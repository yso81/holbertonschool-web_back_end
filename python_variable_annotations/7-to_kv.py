#!/usr/bin/env python3
"""
Function that takes a string and an inr/float as arguemnts and returns a tuple
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[int, float]:
    """
    Takes a string k and an int OR float v as arguments and returns a tuple
    The first element of the tuple is the string k
    The second element is the square of the int/float v
    """
    return (k, v**2)
