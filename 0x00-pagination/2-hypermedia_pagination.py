#!/usr/bin/env python3
"""
Main file
"""
import csv
import math
from typing import List, Tuple, Dict


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
        Initializes the dataset, asserts the correct data type
        and calculates the start an end indexes for the dataset.

        Returns:
            A list of the requested data.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        # initialize the dataset
        dataset = self.dataset()

        start, end = self.index_range(page, page_size)
        length = len(dataset)

        if start > length or end > length:
            return []

        return dataset[start:end]

    def index_range(self, page: int, page_size: int) -> Tuple:
        """
        Returns:
            Atuple containing the start and end indexes of the required data
        """
        start = (page - 1) * page_size
        end = page * page_size

        return (start, end)

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, int]:
        """
        Prepares the pagination for
        Returns:
            A hypermedia pagination as JSON
        """
        dataset = self.get_page(page, page_size)

        total_pages = len(self.dataset()) // page_size
        next_page = None
        prev_page = None

        if page < total_pages:
            next_page = page + 1
        if page > 1:
            prev_page = page - 1

        result = {
            "page_size": page_size,
            "page": page,
            "data": dataset,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }

        return result
