#!/usr/bin/env python3
'''unittesting'''
import unittest
from parameterized import parameterized
from typing import Dict, Union, Tuple
from utilis import access_nested_map, get_json
from unittest.mock import Mock, patch


class TestAccessNestedMap(unittest.TestCase):
    '''Test for acces_nested_map function'''

    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a',), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2)
    ])
    def test_access_nested_map(self,
                               nested_map: Dict,
                               path: Tuple[str],
                               expected: Union[Dict, int]) -> None:
        '''Test access_nested_map'''
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ('a',), KeyError),
        ({'a': 1}, ('a', 'b'), KeyError)
    ])
    def test_access_nested_map_exception(self,
                                         nested_map: Dict,
                                         path: Tuple[str],
                                         expected: Exception) -> None:
        '''Test access_nested_map exception'''
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    '''Testing get_json using mock'''

    @parameterized.expand([
        ("http://example.com", {'playload': True}),
        ("http://holberton.io", {'playload': False})
    ])
    @patch("requests.get")
    def test_get_json(self,
                      test_url: str,
                      test_playload: Dict,
                      mock_get: Mock) -> None:
        '''test get json'''
        mock_response = Mock()
        mock_response.json.return_value = test_playload
        mock_get.return_value = mock_response
        res = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(res, test_playload)
