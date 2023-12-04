import unittest
from fastapi.testclient import TestClient
from unittest.mock import patch

from app.api import app


class TestUserInputEndpoint(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)

    @patch(target='app.db.get_rules_from_database',
           return_value=[("condition1", ["lang1", "lang2"]), ("condition2", ["lang3"])])
    @patch(target='app.inference.infer', return_value="selected_language")
    def test_successful_user_input(self, mock_infer, mock_get_rules):
        response = self.client.get("/user_input?app_type=web&performance=true")
        data = response.json()
        self.assertEqual(first=response.status_code, second=200)
        self.assertEqual(first=data, second={"decision": "selected_language"})
        mock_get_rules.assert_called_once()
        mock_infer.assert_called_once_with({"app_type": "web", "performance": True},
                                           [("condition1", ["lang1", "lang2"]), ("condition2", ["lang3"])])

    @patch(target='app.db.get_rules_from_database',
           return_value=[("condition1", ["lang1", "lang2"]), ("condition2", ["lang3"])])
    @patch(target='app.inference.infer', return_value=None)
    def test_user_input_failure(self, mock_infer, mock_get_rules):
        response = self.client.get("/user_input?app_type=web&performance=true")
        data = response.json()
        self.assertEqual(first=response.status_code, second=400)
        self.assertEqual(first=data, second={"detail": "Sorry, something went wrong."})
        mock_get_rules.assert_called_once()
        mock_infer.assert_called_once_with({"app_type": "web", "performance": True},
                                           [("condition1", ["lang1", "lang2"]), ("condition2", ["lang3"])])


if __name__ == '__main__':
    unittest.main()
