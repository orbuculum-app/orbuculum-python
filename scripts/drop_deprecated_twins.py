"""Leave the deprecated camelCase twins out of the OpenAPI document before generation (BE-307).

Since API 0.179.0 a camelCase read property is declared `deprecated: true` beside its snake_case
twin, which carries the same value. openapi-generator gives both one Python name and collapses them
into a broken field, and a template cannot skip the deprecated one: for a `oneOf` around a `$ref`
the generator drops the `deprecated` flag. scripts/update_api.sh runs this on the downloaded
document, and test/custom/test_openapi_conformance.py reads the recorded document through it.
"""
import json
import re
import sys


def snake_case(name):
    """Return the snake_case twin of a camelCase property name."""
    return re.sub(r"[A-Z]", lambda match: "_" + match.group(0).lower(), name)


def drop_deprecated_twins(document):
    """Delete from `document`, in place, each property marked `deprecated: true` whose snake_case
    twin is a non-deprecated property of the same object, and its name from that object's
    `required`. Return the JSON pointers of the deleted properties. Raise ValueError naming every
    deprecated property without such a twin; the document is then partly filtered: discard it."""
    dropped, orphans = [], []

    def visit(node, where):
        if isinstance(node, list):
            for index, item in enumerate(node):
                visit(item, "%s/%d" % (where, index))
            return
        if not isinstance(node, dict):
            return
        properties = node.get("properties")
        if isinstance(properties, dict):
            for name in [name for name, prop in properties.items() if isinstance(prop, dict) and prop.get("deprecated") is True]:
                twin = snake_case(name)
                if twin == name or not isinstance(properties.get(twin), dict) or properties[twin].get("deprecated"):
                    orphans.append("%s/properties/%s" % (where, name))
                    continue
                del properties[name]
                dropped.append("%s/properties/%s" % (where, name))
                if name in node.get("required", []):
                    node["required"].remove(name)
                    if not node["required"]:
                        del node["required"]
        for key, item in node.items():
            visit(item, "%s/%s" % (where, key))

    visit(document, "#")
    if orphans:
        raise ValueError("Deprecated properties without a snake_case twin: " + ", ".join(orphans))
    return dropped


def main(path):
    with open(path, encoding="utf-8") as spec_file:
        document = json.load(spec_file)
    try:
        dropped = drop_deprecated_twins(document)
    except ValueError as error:
        print("✗ %s" % error)
        return 1
    with open(path, "w", encoding="utf-8") as spec_file:
        json.dump(document, spec_file, ensure_ascii=False)
    print("  Deprecated properties left out of generation: %d" % len(dropped))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
