# coding: utf-8

"""
The generated client against the OpenAPI document it was generated from

The fixture is the document GET /swagger/json served, recorded at the point the
updater consumes it (its own `curl -f -s`), with only example e-mail domains,
one example IP and the server URL substituted. Every other byte, description
text included, is the producer's. The generator copies each description into
the client: a model's class docstring, a field's `description`, an API
method's docstring and the response table of docs/<Tag>Api.md. A client
generated from any other document, or a generator that mangles the text on
the way, fails these rules. The fixture is re-recorded with every regeneration.
"""

import json
import os
import re
import unittest

import orbuculum_client
import orbuculum_client.api as apis
import orbuculum_client.models as models


ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FIXTURE = os.path.join(os.path.dirname(__file__), "fixtures", "openapi_document.json")

HEADER = re.compile(r"^    The version of the OpenAPI document: (.*)$", re.MULTILINE)

# The generator writes no description for a property it turns into a model
# of its own (a reference, a composition or an inline object).
COMPOSED = ("$ref", "allOf", "oneOf", "anyOf", "properties")

# The generator HTML-escapes descriptions in the Markdown docs.
MD_ESCAPE = {"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;", "`": "&#x60;", "=": "&#x3D;"}


def _one_line(text):
    """Return text as the generator writes it into Python source: newlines as spaces."""
    return text.replace("\n", " ")


def _md_escaped(text):
    return "".join(MD_ESCAPE.get(char, char) for char in text)


def _snake(name):
    return re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()


class TestOpenApiConformance(unittest.TestCase):
    """The generated client carries the recorded document's version and descriptions"""

    @classmethod
    def setUpClass(cls):
        with open(FIXTURE, encoding="utf-8") as fixture_file:
            cls.document = json.load(fixture_file)
        cls.operations = [
            (path, method, operation)
            for path, item in cls.document["paths"].items()
            for method, operation in item.items()
            if isinstance(operation, dict) and "operationId" in operation
        ]
        # An inline request body is generated as the model <OperationId>Request;
        # a component schema of that name is shadowed by it and never generated.
        cls.shadowed = {
            operation["operationId"][0].upper() + operation["operationId"][1:] + "Request"
            for _, _, operation in cls.operations
            for content in operation.get("requestBody", {}).get("content", {}).values()
            if "$ref" not in content.get("schema", {})
        }

    def _api(self, operation):
        name = operation["tags"][0].replace(" ", "") + "Api"
        api = getattr(apis, name, None)
        self.assertIsNotNone(api, "no generated %s for %s" % (name, operation["operationId"]))
        return api, name

    def test_api_version_equals_document_version(self):
        version = self.document["info"]["version"]
        self.assertEqual(orbuculum_client.__api_version__, version)
        self.assertEqual(orbuculum_client.__api_supported__, version)
        headers = {}
        for top in ("orbuculum_client", os.path.join("test", "generated")):
            for directory, _, files in os.walk(os.path.join(ROOT, top)):
                for name in files:
                    if name.endswith(".py"):
                        path = os.path.join(directory, name)
                        with open(path, encoding="utf-8") as source:
                            for found in HEADER.findall(source.read()):
                                headers[os.path.relpath(path, ROOT)] = found
        self.assertTrue(headers, "no generated file carries a document version header")
        self.assertEqual({path: found for path, found in headers.items() if found != version}, {})

    def test_model_class_docstrings_equal_schema_descriptions(self):
        for name, schema in self.document["components"]["schemas"].items():
            if "description" not in schema or name in self.shadowed:
                continue
            with self.subTest(schema=name):
                model = getattr(models, name, None)
                self.assertIsNotNone(model, "no generated model %s" % name)
                self.assertEqual((model.__doc__ or "").strip(), _one_line(schema["description"]).strip())

    def test_model_field_descriptions_equal_property_descriptions(self):
        for name, schema in self.document["components"]["schemas"].items():
            if name in self.shadowed:
                continue
            model = getattr(models, name, None)
            self.assertIsNotNone(model, "no generated model %s" % name)
            fields = {field.alias or key: field for key, field in model.model_fields.items()}
            for prop, prop_schema in schema.get("properties", {}).items():
                if "description" not in prop_schema or any(key in prop_schema for key in COMPOSED):
                    continue
                with self.subTest(schema=name, property=prop):
                    self.assertIn(prop, fields)
                    self.assertEqual(fields[prop].description, _one_line(prop_schema["description"]))

    def test_api_method_docstrings_carry_operation_descriptions(self):
        for _, _, operation in self.operations:
            if "description" not in operation:
                continue
            api, _ = self._api(operation)
            for variant in ("", "_with_http_info", "_without_preload_content"):
                method = _snake(operation["operationId"]) + variant
                with self.subTest(method=method):
                    self.assertTrue(hasattr(api, method), "no %s.%s" % (api.__name__, method))
                    lines = [line.strip() for line in (getattr(api, method).__doc__ or "").splitlines()]
                    self.assertIn(_one_line(operation["description"]).strip(), lines)

    def test_api_docs_response_rows_equal_response_descriptions(self):
        for _, _, operation in self.operations:
            _, name = self._api(operation)
            with open(os.path.join(ROOT, "docs", name + ".md"), encoding="utf-8") as doc_file:
                markdown = doc_file.read()
            for code, response in operation.get("responses", {}).items():
                with self.subTest(operation=operation["operationId"], response=code):
                    row = "**%s** | %s | " % (code, _md_escaped(response.get("description", "")))
                    self.assertIn(row, markdown)


if __name__ == '__main__':
    unittest.main()
