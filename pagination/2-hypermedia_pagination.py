#!/usr/bin/env python3
"""
Server class to paginate a database of popular baby names
"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """
    Server class to paginate a database of popular baby names
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
        Takes two integer arguments page with default value 1
        and page_size with default value 10

        Args:
            page (int): The current page number
            page_size (int): Items per page

        Returns:
            List[List]: The correct list of rows (dataset)
        """
        # Validate that inputs are integers and greater than 0
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        # Calculate the start and end index using the index_range function
        range_indexes = index_range(page, page_size)

        start = range_indexes[0]
        end = range_indexes[1]

        # Get the full dataset
        data = self.dataset()

        # Return the appropriate slice
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
         Returns a dictionary with pagination metadata and the dataset slice
        """
        full_dataset = self.dataset()

        total_items = len(full_dataset)
        total_pages = math.ceil(total_items / page_size)

        data = self.get_page(page, page_size)

        if page < total_pages:
            next_page = page + 1
        else:
            next_page = None

        if page > 1:
            prev_page = page - 1
        else:
            prev_page = None

        return {
            "page_size": len(data),  # Actual number of items returned
            "page": page,            # Current page number
            "data": data,            # The list of dataset rows
            "next_page": next_page,  # Navigation to next
            "prev_page": prev_page,  # Navigation to previous
            "total_pages": total_pages # Total available pages
        }
