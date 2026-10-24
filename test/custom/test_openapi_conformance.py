# coding: utf-8

"""
The generated client against the OpenAPI document it was generated from

The fixture is the document GET /swagger/json served, recorded at the point the
updater consumes it (its own `curl -f -s`), with only example e-mail domains,
one example IP and the server URL substituted. Every other byte, description
text included, is the producer's. The generator copies each description into
the client: a model's class docstring, a field's `description`, an API
method's signature and docstring (its operation's parameters, in the
document's order, and their descriptions), the query a call sends, and the
parameter and response tables of docs/<Tag>Api.md. A client
generated from any other document, or a generator that mangles the text on
the way, fails these rules. The fixture is re-recorded with every regeneration.
"""

import datetime
import inspect
import json
import keyword
import os
import re
import typing
import unittest
from types import SimpleNamespace
from unittest import mock
from urllib.parse import parse_qsl, urlsplit

import orbuculum_client
import orbuculum_client.api as apis
import orbuculum_client.models as models
from orbuculum_client import rest


ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FIXTURE = os.path.join(os.path.dirname(__file__), "fixtures", "openapi_document.json")

HEADER = re.compile(r"^    The version of the OpenAPI document: (.*)$", re.MULTILINE)

# The generator writes no description for a property it turns into a model
# of its own (a reference, a composition or an inline object).
COMPOSED = ("$ref", "allOf", "oneOf", "anyOf", "properties")

# The python generator's reserved words: it prefixes a parameter of such a name with `var_`.
RESERVED = frozenset(keyword.kwlist) | {
    "print", "exec", "self", "property", "schema", "base64", "json", "date", "float",
}

# A date the default date format and a day-first one write differently.
DATE = datetime.date(2026, 1, 2)
DATE_FORMAT = "%d.%m.%Y"

# The operations whose bodies the last regeneration changed: each body the
# document declares must reach the caller, and the server, whole.
CHANGED_OPERATIONS = ("getEntities", "createWorkspace")

# The generator HTML-escapes descriptions in the Markdown docs.
MD_ESCAPE = {"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;", "`": "&#x60;", "=": "&#x3D;"}


def _one_line(text):
    """Return text as the generator writes it into Python source: newlines as spaces."""
    return text.replace("\n", " ")


def _md_escaped(text):
    return "".join(MD_ESCAPE.get(char, char) for char in text)


def _snake(name):
    return re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()


def _parameter(name):
    """Return a request parameter's name as the generator writes it: `X-Timezone` as `x_timezone`, `ids[]` as `ids`, `date` as `var_date`."""
    name = re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")
    return "var_" + name if name in RESERVED else name


def _base_type(annotation):
    """Return a parameter's annotation without the generator's `Annotated[..., Field(...)]` wrapper."""
    if typing.get_origin(annotation) is typing.Annotated:
        return typing.get_args(annotation)[0]
    return annotation


def _section(markdown, method):
    """Return the part of docs/<Tag>Api.md under `# **<method>**`, up to the next method heading."""
    match = re.search(r"^# \*\*%s\*\*$(.*?)(?=^# \*\*|\Z)" % re.escape(method), markdown, re.MULTILINE | re.DOTALL)
    return match.group(1) if match else None


def _resolved(document, schema):
    """Return the component schema a `$ref` names, or the schema itself."""
    if "$ref" in schema:
        return document["components"]["schemas"][schema["$ref"].rsplit("/", 1)[-1]]
    return schema


def _example(document, schema, branch, case):
    """Return a body built from the schema's examples, its oneOf as member `branch`.

    `case` varies what the examples alone leave unsaid: `negated` flips every
    boolean, `null` sends every nullable property as null, and `required`
    sends only the required properties (the shape of a server that does not
    know the optional ones yet).
    """
    schema = _resolved(document, schema)
    if "oneOf" in schema:
        return _example(document, schema["oneOf"][branch], branch, case)
    if "properties" in schema:
        return {
            name: _example(document, prop, branch, case)
            for name, prop in schema["properties"].items()
            if case != "required" or name in schema.get("required", ())
        }
    if schema.get("type") == "array":
        return [_example(document, schema["items"], branch, case)]
    if case == "null" and schema.get("nullable"):
        return None
    if case == "negated" and isinstance(schema["example"], bool):
        return not schema["example"]
    return schema["example"]


def _without_nulls(value):
    if isinstance(value, dict):
        return {key: _without_nulls(item) for key, item in value.items() if item is not None}
    if isinstance(value, list):
        return [_without_nulls(item) for item in value]
    return value


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

    def test_changelog_release_supports_document_version(self):
        with open(os.path.join(ROOT, "pyproject.toml"), encoding="utf-8") as pyproject_file:
            package_version = re.search(r'^version = "(.*)"$', pyproject_file.read(), re.MULTILINE)
        self.assertIsNotNone(package_version, "no version in pyproject.toml")
        self.assertEqual(orbuculum_client.__version__, package_version.group(1))
        with open(os.path.join(ROOT, "CHANGELOG.md"), encoding="utf-8") as changelog_file:
            changelog = changelog_file.read()
        version = self.document["info"]["version"]
        # The release's own section, found by its client version: `## <version> — <date> — Supports API <API version>`.
        supported = re.findall(
            r"^## %s — \d{4}-\d{2}-\d{2} — Supports API (.*)$" % re.escape(orbuculum_client.__version__),
            changelog,
            re.MULTILINE,
        )
        self.assertEqual(supported, [version])
        self.assertIn("\n- Regenerated from the API %s OpenAPI specification.\n" % version, changelog)

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

    def test_api_method_parameters_carry_operation_parameters(self):
        for _, _, operation in self.operations:
            api, _ = self._api(operation)
            for parameter in operation.get("parameters", []):
                name = _parameter(parameter["name"])
                for variant in ("", "_with_http_info", "_without_preload_content"):
                    method = _snake(operation["operationId"]) + variant
                    with self.subTest(method=method, parameter=parameter["name"]):
                        self.assertTrue(hasattr(api, method), "no %s.%s" % (api.__name__, method))
                        self.assertIn(name, inspect.signature(getattr(api, method)).parameters)
                        if "description" not in parameter:
                            continue
                        lines = [line.strip() for line in (getattr(api, method).__doc__ or "").splitlines()]
                        # The generator marks a required parameter's description.
                        required = " (required)" if parameter.get("required") else ""
                        self.assertIn((":param %s: %s%s" % (name, _one_line(parameter["description"]), required)).strip(), lines)

    def test_api_method_parameters_follow_operation_order(self):
        for _, _, operation in self.operations:
            api, _ = self._api(operation)
            # The generator puts the required parameters first, each group in the document's order.
            parameters = sorted(operation.get("parameters", []), key=lambda parameter: not parameter.get("required"))
            expected = [_parameter(parameter["name"]) for parameter in parameters]
            for variant in ("", "_with_http_info", "_without_preload_content"):
                method = _snake(operation["operationId"]) + variant
                with self.subTest(method=method):
                    self.assertTrue(hasattr(api, method), "no %s.%s" % (api.__name__, method))
                    found = [name for name in inspect.signature(getattr(api, method)).parameters if name in expected]
                    self.assertEqual(found, expected)

    def test_api_method_date_parameters_are_dates(self):
        for _, _, operation in self.operations:
            api, _ = self._api(operation)
            for parameter in operation.get("parameters", []):
                if parameter.get("schema", {}).get("format") != "date":
                    continue
                name = _parameter(parameter["name"])
                for variant in ("", "_with_http_info", "_without_preload_content"):
                    method = _snake(operation["operationId"]) + variant
                    with self.subTest(method=method, parameter=parameter["name"]):
                        self.assertTrue(hasattr(api, method), "no %s.%s" % (api.__name__, method))
                        signature = inspect.signature(getattr(api, method)).parameters
                        self.assertIn(name, signature)
                        if parameter.get("required"):
                            self.assertEqual(_base_type(signature[name].annotation), datetime.date)
                        else:
                            self.assertEqual(_base_type(signature[name].annotation), typing.Optional[datetime.date])
                            self.assertIsNone(signature[name].default)

    def test_api_calls_send_date_query_parameters_in_date_format(self):
        configuration = orbuculum_client.Configuration(host="https://api.example.com")
        configuration.date_format = DATE_FORMAT
        client = orbuculum_client.ApiClient(configuration)
        for _, _, operation in self.operations:
            query = [parameter for parameter in operation.get("parameters", []) if parameter["in"] == "query"]
            dates = [parameter for parameter in query if parameter.get("schema", {}).get("format") == "date"]
            if not dates:
                continue
            api, _ = self._api(operation)
            method = _snake(operation["operationId"]) + "_without_preload_content"
            # Every required parameter of these operations is an integer query parameter.
            required = {parameter["name"]: 1 for parameter in operation.get("parameters", []) if parameter.get("required")}
            with self.subTest(method=method):
                with mock.patch.object(client, "call_api") as call_api:
                    getattr(api(client), method)(**{_parameter(name): value for name, value in required.items()})
                    sent = parse_qsl(urlsplit(call_api.call_args.args[1]).query)
                    # Without the dates the call sends exactly the parameters it is given.
                    self.assertEqual(sorted(sent), sorted((name, str(value)) for name, value in required.items()))
                    getattr(api(client), method)(
                        **{_parameter(name): value for name, value in required.items()},
                        **{_parameter(parameter["name"]): DATE for parameter in dates}
                    )
                    sent = parse_qsl(urlsplit(call_api.call_args.args[1]).query)
                    for parameter in dates:
                        self.assertIn((parameter["name"], DATE.strftime(DATE_FORMAT)), sent)

    def test_api_docs_parameter_rows_carry_operation_parameters(self):
        for _, _, operation in self.operations:
            _, name = self._api(operation)
            with open(os.path.join(ROOT, "docs", name + ".md"), encoding="utf-8") as doc_file:
                markdown = doc_file.read()
            method = _snake(operation["operationId"])
            section = _section(markdown, method)
            for parameter in operation.get("parameters", []):
                with self.subTest(method=method, parameter=parameter["name"]):
                    self.assertIsNotNone(section, "no section # **%s** in docs/%s.md" % (method, name))
                    parameter_name = _parameter(parameter["name"])
                    rows = [line for line in section.splitlines() if line.startswith(" **%s** | " % parameter_name)]
                    self.assertEqual(len(rows), 1, "no parameter row for %s" % parameter_name)
                    self.assertIn("| %s | " % _md_escaped(_one_line(parameter.get("description", ""))), rows[0])
                    self.assertRegex(section, r"(?m)^    %s = " % re.escape(parameter_name))

    def test_api_docs_response_rows_equal_response_descriptions(self):
        for _, _, operation in self.operations:
            _, name = self._api(operation)
            with open(os.path.join(ROOT, "docs", name + ".md"), encoding="utf-8") as doc_file:
                markdown = doc_file.read()
            for code, response in operation.get("responses", {}).items():
                with self.subTest(operation=operation["operationId"], response=code):
                    row = "**%s** | %s | " % (code, _md_escaped(response.get("description", "")))
                    self.assertIn(row, markdown)

    def _call(self, operation, status, answer, **arguments):
        """Return the body an API method sent, and what it returned, when the server answered `status` with `answer`."""
        api, _ = self._api(operation)
        client = orbuculum_client.ApiClient(orbuculum_client.Configuration(host="https://api.example.com"))
        response = rest.RESTResponse(SimpleNamespace(
            status=status, reason="", data=json.dumps(answer).encode("utf-8"), headers={"content-type": "application/json"},
        ))
        with mock.patch.object(client, "call_api", return_value=response) as call_api:
            returned = getattr(api(client), _snake(operation["operationId"]))(**arguments)
        return call_api.call_args.args[3], client.sanitize_for_serialization(returned)

    def _arguments(self, operation, case):
        """Return a call's arguments, 1 for each required parameter and the request body built from the examples, and that body."""
        arguments = {_parameter(parameter["name"]): 1 for parameter in operation.get("parameters", []) if parameter.get("required")}
        body = None
        for content in operation.get("requestBody", {}).get("content", {}).values():
            name = content["schema"]["$ref"].rsplit("/", 1)[-1]
            body = _example(self.document, content["schema"], 0, case)
            model = getattr(models, name)
            # A caller that leaves a property out builds the model without it.
            arguments[_snake(name)] = model(**body) if case == "required" else model.from_dict(body)
        return arguments, body

    def test_documented_response_bodies_survive_parsing(self):
        for _, _, operation in self.operations:
            if operation["operationId"] not in CHANGED_OPERATIONS:
                continue
            arguments, _ = self._arguments(operation, "examples")
            for code, response in operation["responses"].items():
                if not code.startswith("2"):
                    continue
                schema = _resolved(self.document, response["content"]["application/json"]["schema"])
                for branch in range(len(schema["properties"]["data"].get("oneOf", [None]))):
                    for case in ("examples", "negated", "null", "required"):
                        answer = _example(self.document, schema, branch, case)
                        with self.subTest(operation=operation["operationId"], response=code, branch=branch, case=case):
                            _, returned = self._call(operation, int(code), answer, **arguments)
                            if case == "required":
                                # A property the server did not send reads as unset, never as an error.
                                returned = _without_nulls(returned)
                            self.assertEqual(returned, answer)

    def test_documented_request_bodies_are_sent_whole(self):
        for _, _, operation in self.operations:
            if operation["operationId"] not in CHANGED_OPERATIONS or "requestBody" not in operation:
                continue
            code = next(code for code in operation["responses"] if code.startswith("2"))
            for case in ("examples", "null", "required"):
                arguments, body = self._arguments(operation, case)
                with self.subTest(operation=operation["operationId"], case=case):
                    sent, _ = self._call(operation, int(code), {}, **arguments)
                    # A property the caller did not set is not sent, not even as null.
                    self.assertEqual(sent, body)


if __name__ == '__main__':
    unittest.main()
