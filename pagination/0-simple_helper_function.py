#!/usr/bin/python3
"""
module for pagination
""" 
def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple (start_index, end_index) where start_index is the first item of the
    requested page and end_index is last item of the same requested page.

    Args:
        page: is the requested page
        page_size: is the number of items/lines displayed on the page

    Return:
        tuple: (start_index, end_index)
    """
    start_index = (page-1) * page_size
    end_index = page * page_size

    return (start_index, end_index)
