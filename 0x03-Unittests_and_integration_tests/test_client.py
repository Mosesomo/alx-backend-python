#!/usr/bin/env python3
'''Client'''
import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock, Mock
from client import GithubOrgClient
from utils import (
    get_json,
    access_nested_map,
    memoize,
)


class TestGithubOrgClient(unittest.TestCase):
    '''Testing github organization client'''
    @parameterized.expand([
        ('google'),
        ('abc'),
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str,
                 mock_get_json: Mock) -> None:
        '''Test github organization'''
        mock_get_json.return_value = {
            'name': org_name,
            'resp_url': f'https://api.github.com/orgs/{org_name}/repos'
        }

        git_client = GithubOrgClient(org_name)
        org_info = git_client.org
        mock_get_json.assert_called_once_with(
            f'https://api.github.com/orgs/{org_name}')
        self.assertEqual(org_info['name'], org_name)

    def test_public_repos_url(self) -> None:
        '''Test public repos url'''
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {
                'repos_url': 'https://api.github.com/orgs/google/repos'
            }

            git_client = GithubOrgClient('google')
            public_repos_url = git_client._public_repos_url
            self.assertEqual(public_repos_url,
                             'https://api.github.com/orgs/google/repos')
