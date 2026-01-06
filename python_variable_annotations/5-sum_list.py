#!/usr/bin/env python3
"""
Function that takes a list of floats and returns the sum of its float
"""
from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Function that returns the sum(float) of a list of floats

    Args:
    input_list: list[float]

    Returns:
    sum of input_list: float
    """
    return sum(input_list)
