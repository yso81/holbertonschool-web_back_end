#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> dict:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> dict:
        """
        The goal here is that if between two queries, certain rows are removed
        from the dataset, the user does not miss items from dataset when
        changing page

        Args:
            index (int): The starting index of the page (None defaults to 0)
            page_size (int): The number of items to retrieve.

        Returns:
            Dict: containing index, next_index, page_size, and data
        """
        dataset = self.indexed_dataset()

        if index is None:
            index = 0

        assert 0 <= index <= max(dataset.keys())

        current_index = index
        data = []
        next_index = index

        while len(data) < page_size and next_index <= max(dataset.keys()):
            if next_index in dataset:
                data.append(dataset[next_index])

        next_index += 1

        return {
            "index": index,          # The requested start index
            "next_index": next_index,  # The index to use for the NEXT request
            "page_size": len(data),   # The actual size of the page returned
            "data": data
        }
