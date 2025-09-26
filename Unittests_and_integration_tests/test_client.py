#!/usr/bin/env python3
"""
Unit tests for client.GithubOrgClient
"""
import unittest
from unittest.mock import patch, PropertyMock
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

        client_obj = GithubOrgClient(org_name)
        result = client_obj.org

        mock_get_json.assert_called_once()
        self.assertEqual(result, test_payload)

    def test_public_repos_url(self):
        """Test that _public_repos_url returns the expected URL"""
        # Fake payload that GithubOrgClient.org would normally return
        test_payload = {"repos_url": "https://api.github.com/orgs/google/repos"}

        with patch.object(
            GithubOrgClient,
            "org",
            new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = test_payload

            client_obj = GithubOrgClient("google")
            result = client_obj._public_repos_url

            # Ensure _public_repos_url matches repos_url from the mocked payload
            self.assertEqual(result, test_payload["repos_url"])
            mock_org.assert_called_once()


if __name__ == "__ma
