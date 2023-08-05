#!/usr/bin/env python3
"""
    unittest for client module using parameterized.
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient
from utils import get_json


class TestGithubOrgClient(unittest.TestCase):
    """
        a class that test org function in GithubOrgClient

        Args:
            unittest (object): Unittest Base
        """
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch("client.get_json")
    def test_org(self, org, mock_js):
        """
            test org function runs successfully

            Args:
                org (str): the org name
                mock_js (obj): mocked data
        """
        endpoint = GithubOrgClient.ORG_URL.format(org=org)
        model = GithubOrgClient(org)
        model.org()
        mock_js.assert_called_once_with(endpoint)

    @parameterized.expand([
        ("random-url", {'repos_url': 'http://some_url.com'})
    ])
    def test_public_repos_url(self, name, result):
        """ Test method returns correct output """
        with patch('client.GithubOrgClient.org',
                   PropertyMock(return_value=result)):
            response = GithubOrgClient(name)._public_repos_url
            self.assertEqual(response, result.get('repos_url'))

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """
        Test that the list of repos is what you expect from the chosen payload.
        Test that the mocked property and the mocked get_json was called once.
        """
        json_payload = [{"name": "Google"}, {"name": "Twitter"}]
        mock_json.return_value = json_payload

        with patch('client.GithubOrgClient._public_repos_url',
                new_callable=PropertyMock) as mock_public:

            mock_public.return_value = "hello/world"
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()

            check = [i["name"] for i in json_payload]
            self.assertEqual(result, check)

            mock_public.assert_called_once()
            mock_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """
            test to check license
        Args:
            repo (Dict[str, Dict]): repo
            license_key (str): license key
            expected (Bool): True or False
        """
        self.assertEqual(GithubOrgClient.has_license(repo, license_key),
                         expected)
