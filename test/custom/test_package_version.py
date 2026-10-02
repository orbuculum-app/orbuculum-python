# coding: utf-8

"""
Version attributes of the imported orbuculum_client package

At runtime the package is replaced with a lazy_imports.LazyModule that carries
only the names passed to it, so each documented version attribute must be
reachable on the imported package, and must equal the literal of its column-0
assignment in the __init__.py the package was imported from.
"""

import re
import unittest

import orbuculum_client


VERSION_ATTRIBUTES = ("__version__", "__api_version__", "__api_supported__")


def _assigned_literal(source, name):
    """Return the literal of the column-0 `<name> = "..."` line in source."""
    match = re.search(r'^' + re.escape(name) + r' = "(.*)"$', source, re.MULTILINE)
    return match.group(1) if match else None


class TestPackageVersion(unittest.TestCase):
    """The package's version attributes after a plain import"""

    @classmethod
    def setUpClass(cls):
        with open(orbuculum_client.__file__, encoding="utf-8") as init_file:
            cls.init_source = init_file.read()

    def test_version_attributes_are_non_empty_strings(self):
        for name in VERSION_ATTRIBUTES:
            with self.subTest(name=name):
                self.assertTrue(
                    hasattr(orbuculum_client, name),
                    "orbuculum_client.%s is not reachable on the imported package" % name,
                )
                value = getattr(orbuculum_client, name)
                self.assertIsInstance(value, str)
                self.assertNotEqual(value, "")

    def test_version_attributes_equal_init_assignments(self):
        for name in VERSION_ATTRIBUTES:
            with self.subTest(name=name):
                expected = _assigned_literal(self.init_source, name)
                self.assertIsNotNone(
                    expected,
                    "no column-0 %s assignment in %s" % (name, orbuculum_client.__file__),
                )
                self.assertEqual(getattr(orbuculum_client, name, None), expected)


if __name__ == '__main__':
    unittest.main()
