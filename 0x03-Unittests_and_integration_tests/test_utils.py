#!/usr/bin/env python3
'''unittesting'''
import unittest
from parameterized import parameterized
from typing import Dict, Union, Tuple
from utilis import access_nested_map


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
