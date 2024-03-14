#!/usr/bin/env python3
"""importing modules"""
from typing import List, Any, Tuple


def element_length(lst: List[Any]) -> List[Tuple[Any, int]]:
    """return values with the appropriate types"""

    return [(i, len(i)) for i in lst]
