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
        unittest (object): Unittest base
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested, path, expected):
        """
            test if the expected value is equal to the main value

            Args:
                nested (Mapping): the nested mapped argument
                path (Sequence): containing the nested dict keys
                expected (int): the output from the function
        """
        self.assertEqual(access_nested_map(nested, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested, path):
        """
            test if the raised KeyError exception will properly be displayed

            Args:
                nested (Mapping): the nested mapped argument.
                path (Sequence): containing the nested dict keys.
        """
        self.assertRaises(KeyError, access_nested_map, nested, path)
