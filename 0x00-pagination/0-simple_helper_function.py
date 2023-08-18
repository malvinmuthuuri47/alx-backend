#!/usr/bin/env python3
from typing import Tuple
"""This module calculates the indexes used for pagination"""


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        A function that takes two args, computes the start and end
        indexes and returns a tuple containing the start and end idx

        Args:
            page: Page no.
            page_size: Size of the page

        Returns:
            A Tupleof size two[start_idx, end_idx]
    """
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    return start_idx, end_idx
