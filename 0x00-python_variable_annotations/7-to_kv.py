#!/usr/bin/env python3

"""
type-annotated function to_kv that takes
a string k and an int OR float v as arguments
and returns a tuple.
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:

    """
    Take a string and an int or float and return a tuple.
    Parameters:
    k (str): The string to include in the tuple.
    v (Union[int, float]): The int or float to square.

    Returns:
    Tuple[str, float]: A tuple with the string k and the square of v as a
        float.
    """

    return (k, float(v ** 2))
