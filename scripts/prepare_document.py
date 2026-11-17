"""The OpenAPI document as the generator reads it, prepared in two passes before generation.

Deprecated twins (BE-307). Since API 0.179.0 a camelCase read property is declared
`deprecated: true` beside its snake_case twin, which carries the same value. openapi-generator gives
both one Python name and collapses them into a broken field, and a template cannot skip the
deprecated one: for a `oneOf` around a `$ref` the generator drops the `deprecated` flag.

Example addresses. The generator copies `example` values into test/generated, and the addresses
there must pass the address rule: an IPv4 address outside 0.0.0.0/8 and 127.0.0.0/8 gets first
octet 0, and an e-mail address on a non-reserved domain gets the domain example.net. Only values
under an `example` or `examples` keyword are rewritten, never descriptions or `servers[].url`.

scripts/update_api.sh runs this on the downloaded document, and
test/custom/test_openapi_conformance.py reads the recorded document through it.
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


_IPV4 = re.compile(r"(?<![\d.])(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})(?![\d.])")
_EMAIL_DOMAIN = re.compile(r"(?<=[A-Za-z0-9._%+-])@([A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+)")
_RESERVED = ("example.com", "example.org", "example.net")


def _address(match):
    if any(int(octet) > 255 for octet in match.groups()) or match.group(1) in ("0", "127"):
        return match.group(0)
    return "0." + ".".join(match.groups()[1:])


def _domain(match):
    domain = match.group(1).lower()
    if domain in _RESERVED or domain.endswith(tuple("." + d for d in _RESERVED)) \
            or domain.endswith((".example", ".test", ".invalid")) or domain == "localhost":
        return match.group(0)
    return "@example.net"


def substitute_examples(document):
    """In place: rewrite addresses in example values; return the JSON pointers of the values rewritten."""
    rewritten = []

    def rewrite(value):
        if isinstance(value, str):
            return _EMAIL_DOMAIN.sub(_domain, _IPV4.sub(_address, value))
        if isinstance(value, list):
            return [rewrite(item) for item in value]
        if isinstance(value, dict):
            return {key: rewrite(item) for key, item in value.items()}
        return value

    def visit(node, where, names):  # names: node's keys are property names, not keywords
        if isinstance(node, dict):
            for key, value in node.items():
                pointer = "%s/%s" % (where, key)
                if not names and key in ("example", "examples"):
                    new = rewrite(value)
                    if new != value:
                        node[key] = new
                        rewritten.append(pointer)
                else:
                    visit(value, pointer, key == "properties")
        elif isinstance(node, list):
            for index, item in enumerate(node):
                visit(item, "%s/%d" % (where, index), False)

    visit(document, "#", False)
    return rewritten


def main(path):
    with open(path, encoding="utf-8") as spec_file:
        document = json.load(spec_file)
    try:
        dropped = drop_deprecated_twins(document)
    except ValueError as error:
        print("✗ %s" % error)
        return 1
    substituted = substitute_examples(document)
    with open(path, "w", encoding="utf-8") as spec_file:
        json.dump(document, spec_file, ensure_ascii=False)
    print("  Deprecated properties left out of generation: %d" % len(dropped))
    print("  Example values with addresses substituted: %d" % len(substituted))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
