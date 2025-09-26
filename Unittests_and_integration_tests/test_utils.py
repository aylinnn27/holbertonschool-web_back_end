import unittest
from unittest.mock import patch, Mock
from utils import get_json

class TestGetJson(unittest.TestCase):
    @patch("utils.requests.get")
    def test_get_json(self, mock_get):
        # First test case
        test_url = "http://example.com"
        test_payload = {"payload": True}

        # Mock setup: requests.get(url).json() should return test_payload
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Call the function being tested
        result = get_json(test_url)

        # Assertions
        mock_get.assert_called_once_with(test_url)   # ensure requests.get called with url
        self.assertEqual(result, test_payload)       # ensure return value matches mock payload
