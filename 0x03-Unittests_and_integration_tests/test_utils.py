#!/usr/bin/env python3
"""
    unittest for utils.access_nested_map function using parameterized
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
        a class that test the accessnestedmap function from utils
    Args:
        unittest (_type_): _description_
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), 2),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested, path, expected):
        """ test for access_nested_map """
        self.assertEqual(access_nested_map(nested, path), expected)
