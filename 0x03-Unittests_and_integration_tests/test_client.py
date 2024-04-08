#!/usr/bin/env python3
'''Client'''
import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock, Mock
from client import GithubOrgClient
from typing import Dict


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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json: Mock) -> None:
        '''Public repos'''
        mock_get_json.return_value = [
            {'name': 'repo1', 'license': {'key': 'mit'}},
            {'name': 'repo2', 'license': {'key': 'apache-2.0'}},
            {'name': 'repo3', 'license': {'key': 'gpl-3.0'}}
        ]
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_get_public_repos:
            mock_get_public_repos.\
                return_value = 'https://api.github.com/orgs/google/repos'
            git_client = GithubOrgClient('google')
            repos = git_client.public_repos()
            expected_repos = ['repo1', 'repo2', 'repo3']
            self.assertEqual(repos, expected_repos)
            mock_get_public_repos.assert_called_once()

    @parameterized.expand([
        ({'license': {'key': 'my_license'}}, 'my_license', True),
        ({'license': {'key': 'other_license'}}, 'my_license', False),
    ])
    def test_has_license(self, repo: Dict,
                         key: str, expected: bool) -> None:
        '''Test for `has_license` method'''
        git_client = GithubOrgClient('google')
        has_license = git_client.has_license(repo, key)
        self.assertEqual(has_license, expected)
