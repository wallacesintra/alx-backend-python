#!/usr/bin/env python3

"""
element length module
"""

from typing import List, Sequence, Union, Any


def element_length(lst: Sequence[Union[Any, str]]) -> List[int]:
    """
    Return a list of the lengths of each element in lst.
    """
    return [len(i) for i in lst]
