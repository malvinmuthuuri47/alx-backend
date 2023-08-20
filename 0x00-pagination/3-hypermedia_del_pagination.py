#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_names.csv"

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

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """A function that returns a dictionary with key-value pairs"""
        assert index is None or isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0

        indexed_dataset = self.indexed_dataset()
        total_items = len(indexed_dataset)

        if index is None:
            index = 0
        elif index >= total_items:
            return {}

        next_index = min(index + page_size, total_items)
        data = [indexed_dataset.get(i) for i in range(index, next_index)
                if i in indexed_dataset]

        return {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": data
        }