#!/usr/bin/env python3
"""
    unittest for client module using parameterized.
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


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
        """
        endpoint = GithubOrgClient.ORG_URL.format(org=org)
        model = GithubOrgClient(org)
        model.org()
        mock_js.assert_called_once_with(endpoint)
