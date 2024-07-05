#!/usr/bin/env python3

"""
type-annotated function sum_list that takes
a list input_list of floats as argument
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return the sum of a list of floats"""
    return sum(input_list)
