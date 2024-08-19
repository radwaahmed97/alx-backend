#!/usr/bin/env python3
"""contains function index_range(page: int, page_size: int)"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    return a tuple of size two containing a start index
    and an end index corresponding to the range of indexes to
    return in a list for those particular pagination parameters.
    """
    start_of_page = (page - 1) * page_size
    end_of_page = start_of_page + page_size
    return (start_of_page, end_of_page)
