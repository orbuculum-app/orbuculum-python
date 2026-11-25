"""
Parsing of GET /api/reports/get-pnl, get-balances and get-cashflow 200 bodies

Bodies recorded from the monolith at API 0.201.0 (names substituted). BE-428 made every
amount a decimal string of any scale, kept as that exact str; an int (0.199.0) must not parse.
"""

import json
import os
import unittest

from pydantic import ValidationError

from orbuculum_client.api_client import ApiClient


FIXTURES = os.path.join(os.path.dirname(__file__), "fixtures")

# (report, response model, path of one amount under data.periods[0], the sub-model that owns it)
REPORTS = (
    ("pnl", "PnlReportResponse", ("forex",), "PnlReportResponseDataPeriodsInner"),
    ("balances", "BalancesReportResponse", ("debit", "total"), "BalancesReportResponseDataPeriodsInnerDebit"),
    ("cashflow", "CashflowReportResponse", ("totals", "free_cash"), "CashflowReportResponseDataPeriodsInnerTotals"),
)


def _strings(node, path=()):
    """Yield (path, value) for every string leaf of a raw JSON body."""
    if isinstance(node, str):
        yield path, node
    elif isinstance(node, (dict, list)):
        for key, value in (node.items() if isinstance(node, dict) else enumerate(node)):
            yield from _strings(value, path + (key,))


def _at(node, path):
    """Follow a path through raw JSON (keys, indexes) or a parsed model (attribute names)."""
    for key in path:
        node = node[key] if isinstance(node, (dict, list)) else getattr(node, key)
    return node


class TestReportParsing(unittest.TestCase):
    """The three report response models against recorded 0.201.0 bodies"""

    def _recorded(self, report):
        with open(os.path.join(FIXTURES, "reports_get_%s_200.json" % report), encoding="utf-8") as fixture_file:
            return fixture_file.read()

    def test_recorded_amounts_come_back_as_the_same_strings(self):
        for report, model, path, _ in REPORTS:
            with self.subTest(report=report):
                text = self._recorded(report)
                sent = dict(_strings(json.loads(text)["data"]["periods"]))
                self.assertTrue("0" in sent.values() and any(v[:1] == "-" and "." in v for v in sent.values()))
                periods = ApiClient().deserialize(text, model, "application/json").data.periods
                parsed = ApiClient().sanitize_for_serialization(periods)
                self.assertEqual({p: _at(parsed, p) for p in sent}, sent)
                self.assertIs(type(_at(periods[0], path)), str)

    def test_integer_amount_is_rejected(self):
        for report, model, path, owner in REPORTS:
            with self.subTest(report=report):
                body = json.loads(self._recorded(report))
                _at(body["data"]["periods"][0], path[:-1])[path[-1]] = 7
                with self.assertRaises(ValidationError) as caught:
                    ApiClient().deserialize(json.dumps(body), model, "application/json")
                self.assertEqual(caught.exception.title, owner)
                self.assertEqual([(e["loc"], e["type"]) for e in caught.exception.errors()], [(path[-1:], "string_type")])
