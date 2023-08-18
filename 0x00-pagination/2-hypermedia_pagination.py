#!/usr/bin/env python3
"""Hypermedia Pagination"""
import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        A function that takes two args, computes the start and end
        indexes and returns a tuple containing the start and end idx

        Args:
            page: Page no.
            page_size: Size of the page

        Returns:
            A Tuple of size two[start_idx, end_idx]
    """
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    return start_idx, end_idx


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_names.csv"

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
            A function that calls the index_page() to handle the pagination
            and returns a list if the index isn't out of range and otherwise,
            returns an empty list
        """
        assert isinstance(page, int) and page > 0, "should_err"
        assert isinstance(page_size, int) and page_size > 0, "should_err"

        start_idx, end_idx = index_range(page, page_size)
        dataset = self.dataset()

        if start_idx >= len(dataset):
            return []

        return dataset[start_idx:end_idx]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[int, List]:
        """
            This function takes page and page_size and returns a dictionary
            containing key-value pairs
        """
        assert isinstance(page, int) and page > 0, "should_err"
        assert isinstance(page_size, int) and page_size > 0, "should_err"

        dataset_page = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
                "page_size": len(dataset_page),
                "page": page,
                "data": dataset_page,
                "next_page": next_page,
                "prev_page": prev_page,
                "total_pages": total_pages
        }
