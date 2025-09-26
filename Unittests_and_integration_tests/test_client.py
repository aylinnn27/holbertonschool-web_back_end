#!/usr/bin/env python3
"""
Unit tests for client.GithubOrgClient
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        test_payload = {"login": org_name}

        # Configure the mock to return the test payload
        mock_get_json.return_value = test_payload

        # Instantiate the client with the test org
        client_obj = GithubOrgClient(org_name)

        # Access the org property
        result = client_obj.org

        # Assert get_json was called once with the correct URL
        mock_get_json.assert_called_once()

        # Assert that the returned result matches the mock payload
        self.assertEqual(result, test_payload)


if __name__ == "__main__":
    unittest.main()
