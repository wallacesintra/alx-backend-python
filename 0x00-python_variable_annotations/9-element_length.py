#!/usr/bin/env python3

"""
element length module
"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of the lengths of each element in lst.
    """

    return [len(i) for i in lst]
