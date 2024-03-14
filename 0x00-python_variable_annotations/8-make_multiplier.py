#!/usr/bin/env python3
"""importing modules"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        type-annotated function make_multiplier
        that takes a float multiplier as argument
        and returns a function that multiplies a
        float by multiplier
    """

    def func(value: float) -> float:
        return value * multiplier
    return func
