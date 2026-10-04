# coding: utf-8

"""
Parsing of POST /api/transaction-draft 200 bodies

The fixture is a 200 body recorded from the monolith serving API 0.144.0
(label names substituted), so the shape under test is the producer's, not
ours. Every `selectable[]` entry carries the required boolean `recent`; a
body or entry without it (the API 0.143.0 shape) must not parse.
"""

import copy
import json
import os
import unittest

from pydantic import ValidationError

from orbuculum_client.api_client import ApiClient
from orbuculum_client.models.transaction_draft_selectable_account import TransactionDraftSelectableAccount


FIXTURE = os.path.join(os.path.dirname(__file__), "fixtures", "transaction_draft_200.json")

SLOTS = ("sender", "receiver", "double")


def _filled_slots(form):
    """Return (name, raw slot) for each slot of a raw form that is not null."""
    return [(name, form[name]) for name in SLOTS if form.get(name) is not None]


class TestTransactionDraftParsing(unittest.TestCase):
    """TransactionDraftSelectableAccount and TransactionDraftResponse against a recorded 0.144.0 body"""

    @classmethod
    def setUpClass(cls):
        with open(FIXTURE, encoding="utf-8") as fixture_file:
            cls.body_text = fixture_file.read()
        cls.body = json.loads(cls.body_text)
        cls.entries = [
            entry
            for _, slot in _filled_slots(cls.body["data"]["form"])
            for entry in slot["selectable"]
        ]

    def _deserialize(self, text):
        return ApiClient().deserialize(text, "TransactionDraftResponse", "application/json")

    def test_selectable_entry_keeps_recent(self):
        sent = {entry["recent"] for entry in self.entries}
        self.assertEqual(sent, {True, False}, "the recorded body must carry both recent values")
        self.assertEqual(
            [(e["account_id"], TransactionDraftSelectableAccount.from_dict(e).recent) for e in self.entries],
            [(e["account_id"], e["recent"]) for e in self.entries],
        )

    def test_selectable_entry_without_recent_is_rejected(self):
        for recent in (True, False):
            entry = next(e for e in self.entries if e["recent"] is recent)
            absent = {key: value for key, value in entry.items() if key != "recent"}
            null = dict(entry, recent=None)
            for case, old in (("absent", absent), ("null", null)):
                with self.assertRaises(ValidationError, msg="recorded recent=%s, %s" % (recent, case)):
                    TransactionDraftSelectableAccount.from_dict(old)

    def test_response_keeps_recent_of_every_entry(self):
        response = self._deserialize(self.body_text)
        form = response.data.form
        raw_form = self.body["data"]["form"]
        self.assertEqual(
            [name for name in SLOTS if getattr(form, name) is not None],
            [name for name, _ in _filled_slots(raw_form)],
        )
        self.assertEqual(
            {name: [(e.account_id, e.recent) for e in getattr(form, name).selectable] for name, _ in _filled_slots(raw_form)},
            {name: [(e["account_id"], e["recent"]) for e in slot["selectable"]] for name, slot in _filled_slots(raw_form)},
        )

    def test_response_without_recent_is_rejected(self):
        old = copy.deepcopy(self.body)
        for _, slot in _filled_slots(old["data"]["form"]):
            for entry in slot["selectable"]:
                del entry["recent"]
        with self.assertRaises(ValidationError):
            self._deserialize(json.dumps(old))


if __name__ == '__main__':
    unittest.main()
