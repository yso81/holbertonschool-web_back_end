#!/usr/bin/env python3
import csv
import math
from typing import List
"""
A module that paginates through a dataset with starting page = 1 and page_size = 10
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple (start_index, end_index) where start_index is the first
    item of the requested page and end_index is last item of the same requested
    page.

    Args:
        page: is the requested page
        page_size: is the number of items/lines displayed on the page

    Return:
        tuple: (start_index, end_index)
    """
    start_index = (page-1) * page_size
    end_index = page * page_size

    return (start_index, end_index)

class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Module that takes 2 arguments, default page = 1 and fixed page size =10
        and return a list

        Args:
            page: int = 1, the current page number that is greater than 0 and
            not negative
        
        Returns:
            List[]: The extracted list of items from the dataset
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        data = self.dataset

        pages = index_range(page, page_size)

        start_page = pages[0]
        end_page = pages[1]



        return data[start_page, end_page]
