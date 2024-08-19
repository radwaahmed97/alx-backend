#!/usr/bin/env python3
"""
method named get_page that takes two integer arguments page
with default value 1 and page_size with default value 10.
"""

from typing import Tuple
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    return a tuple of size two containing a start index
    and an end index corresponding to the range of indexes to
    return in a list for those particular pagination parameters.
    """
    start_of_page = (page - 1) * page_size
    end_of_page = start_of_page + page_size
    return (start_of_page, end_of_page)


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
        returns appropriate page of the dataset
        and empty list in case of arguments out of range
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start_of_page, end_of_page = index_range(page, page_size)
        retrieved_data = self.dataset()
        if start_of_page > len(retrieved_data):
            return []
        return retrieved_data[start_of_page:end_of_page]
