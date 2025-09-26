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
        mock_get_json.return_value = test_payload

        client_obj = GithubOrgClient(org_name)
        result = client_obj.org

        mock_get_json.assert_called_once()
        self.assertEqual(result, test_payload)

    def test_public_repos_url(self):
        """Test that _public_repos_url returns the expected URL"""
        test_payload = {
            "repos_url": "https://api.github.com/orgs/google/repos"
        }

        with patch.object(
            GithubOrgClient,
            "org",
            new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = test_payload

            client_obj = GithubOrgClient("google")
            result = client_obj._public_repos_url

            self.assertEqual(result, test_payload["repos_url"])
            mock_org.assert_called_once()

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """Test that public_repos returns the expected list of repos"""
        # Fake repo payload returned by get_json
        test_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]
        mock_get_json.return_value = test_payload

        # Patch _public_repos_url to return a dummy URL
        with patch.object(
            GithubOrgClient,
            "_public_repos_url",
            new_callable=PropertyMock
        ) as mock_repos_url:
            mock_repos_url.return_value = (
                "https://api.github.com/orgs/google/repos"
            )

            client_obj = GithubOrgClient("google")
            result = client_obj.public_repos()

            # Expect list of repo names only
            expected = ["repo1", "repo2", "repo3"]
            self.assertEqual(result, expected)

            # Ensure both mocks were called once
            mock_repos_url.assert_called_once()
            mock_get_json.assert_called_once()


if __name__ == "__main__":
    unittest.main()
