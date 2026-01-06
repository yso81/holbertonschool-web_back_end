#!/usr/bin/env python3
"""
Function that takes a list mxd_lst of integers and floats and returns their sum
as a float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """
    Function that returns the sum of the elements

    Args:
    mxd_lst[List[float, int]]: is a list of different types of elements.

    Return:
    SUm of elements: float
    """
    return float(sum(mxd_lst))
