#!/usr/bin/env python3
"""Importing module"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Function that return the sum of integers and floats
    arguments:
    mxd_lst: list of integers and floats
    Return: sum
    """

    return sum(mxd_lst)
