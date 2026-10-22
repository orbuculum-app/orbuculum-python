# coding: utf-8

"""
Parsing of GET /api/workspace/context 200 bodies

The fixture is a 200 body recorded from the monolith after BE-163 (project
names and the rules hash substituted), so the shape under test is the
producer's, not ours. The document declares every map `type: object`, and
the monolith sends an empty one as `{}`: a label without account
limitations is `{}` in `account_limitation_filtering`. A body that sends
such an entry as `[]` (the pre-BE-163 shape) must not parse, and the client
carries no workaround for it. `transaction_rules.vocabulary.base_subtabs`
maps each tab to a list of sub-tabs, and every sub-tab of every list is
checked against the sub-tab enum.
"""

import copy
import json
import os
import unittest

from pydantic import ValidationError

from orbuculum_client.api_client import ApiClient


FIXTURE = os.path.join(os.path.dirname(__file__), "fixtures", "workspace_context_200.json")


def _empty_labels(filtering):
    """Return the label IDs whose raw account_limitation_filtering entry is an empty map."""
    return [label for label, accounts in filtering.items() if accounts == {}]


class TestWorkspaceContextParsing(unittest.TestCase):
    """WorkspaceContextResponse against a recorded post-BE-163 body"""

    @classmethod
    def setUpClass(cls):
        with open(FIXTURE, encoding="utf-8") as fixture_file:
            cls.body_text = fixture_file.read()
        cls.body = json.loads(cls.body_text)
        cls.data = cls.body["data"]

    def _deserialize(self, text):
        return ApiClient().deserialize(text, "WorkspaceContextResponse", "application/json")

    def test_recorded_body_parses(self):
        self.assertTrue(_empty_labels(self.data["account_limitation_filtering"]), "the recorded body must carry a label without limitations")
        response = self._deserialize(self.body_text)
        self.assertEqual(response.status, self.body["status"])
        self.assertEqual(response.data.transaction_rules_version, self.data["transaction_rules_version"])

    def test_account_types_keep_every_field(self):
        raw = self.data["account_types"]
        parsed = self._deserialize(self.body_text).data.account_types
        self.assertEqual(
            {account: {field: getattr(entry, field) for field in raw[account]} for account, entry in parsed.items()},
            raw,
        )

    def test_maps_keep_their_entries(self):
        data = self._deserialize(self.body_text).data
        for field in ("account_limitation_filtering", "rates_by_date"):
            with self.subTest(field=field):
                self.assertEqual(getattr(data, field), self.data[field])
        self.assertEqual(
            {label: data.account_limitation_filtering[label] for label in _empty_labels(self.data["account_limitation_filtering"])},
            {label: {} for label in _empty_labels(self.data["account_limitation_filtering"])},
        )

    def test_empty_map_sent_as_list_is_rejected(self):
        self._deserialize(self.body_text)
        filtering = self.data["account_limitation_filtering"]
        label = _empty_labels(filtering)[0]
        nested_label, nested_accounts = next((key, value) for key, value in filtering.items() if value)
        nested_account = next(iter(nested_accounts))
        for case, path in (("label", (label,)), ("account", (nested_label, nested_account))):
            old = copy.deepcopy(self.body)
            target = old["data"]["account_limitation_filtering"]
            for key in path[:-1]:
                target = target[key]
            target[path[-1]] = []
            with self.assertRaises(ValidationError, msg=case):
                self._deserialize(json.dumps(old))

    def test_base_subtab_outside_the_enum_is_rejected(self):
        raw = self.data["transaction_rules"]["vocabulary"]["base_subtabs"]
        parsed = self._deserialize(self.body_text).data.transaction_rules.vocabulary.base_subtabs
        self.assertEqual(parsed, raw)
        longest = max(raw, key=lambda tab: len(raw[tab]))
        shortest = min(raw, key=lambda tab: len(raw[tab]))
        for case, tab in (("last of the longest list", longest), ("only item of the shortest list", shortest)):
            old = copy.deepcopy(self.body)
            subtabs = old["data"]["transaction_rules"]["vocabulary"]["base_subtabs"][tab]
            subtabs[-1] = subtabs[-1] + "s"
            with self.assertRaises(ValidationError, msg=case):
                self._deserialize(json.dumps(old))


if __name__ == '__main__':
    unittest.main()
