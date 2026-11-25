"""
Serialisation of POST /api/matching/suggest request bodies

as_of and exclude_transaction_ids (BE-424, BE-426) as sent: sanitize_for_serialization writes a
datetime as isoformat(); to_json() cannot encode one, so only a request without as_of uses it.
"""

import json
import unittest
from datetime import datetime, timezone

from orbuculum_client.api_client import ApiClient
from orbuculum_client.models.matching_suggest_request import MatchingSuggestRequest


AS_OF = datetime(2026, 11, 1, 12, 0, tzinfo=timezone.utc)


class TestMatchingSuggestSerialization(unittest.TestCase):
    """MatchingSuggestRequest with and without as_of and exclude_transaction_ids"""

    def test_as_of_and_excluded_ids_are_sent(self):
        request = MatchingSuggestRequest(workspace_id=1, as_of=AS_OF, exclude_transaction_ids=[7, 9])
        body = ApiClient().sanitize_for_serialization(request)
        self.assertEqual((body["as_of"], body["exclude_transaction_ids"]), ("2026-11-01T12:00:00+00:00", [7, 9]))
        self.assertEqual({k: request.to_dict()[k] for k in ("as_of", "exclude_transaction_ids")}, {"as_of": AS_OF, "exclude_transaction_ids": [7, 9]})

    def test_both_fields_may_be_omitted(self):
        request = MatchingSuggestRequest(workspace_id=1)
        self.assertEqual((request.as_of, request.exclude_transaction_ids), (None, None))
        for sent in (request.to_dict(), json.loads(request.to_json()), ApiClient().sanitize_for_serialization(request)):
            self.assertEqual(sent, {"workspace_id": 1, "limit": 5})
