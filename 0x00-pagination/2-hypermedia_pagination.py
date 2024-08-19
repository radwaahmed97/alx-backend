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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
         returns a dictionary containing the following key-value pair
         page_size: the length of the returned dataset page
         page: the current page number
         data: the dataset page (equivalent to return from previous task)
         next_page: number of the next page, None if no next page
         prev_page: number of the previous page, None if no previous page
         total_pages: the total number of pages in the dataset as an integer
        """
        data_of_page = self.get_page(page, page_size)
        start_of_page, end_of_page = index_range(page, page_size)
        all_pages = math.ceil(len(self.__dataset) / page_size)
        page_mapping = {
                'page_size': len(data_of_page),
                'page': page,
                'data': data_of_page,
                'next_page': page + 1 if end_of_page <
                len(self.__dataset) else None,
                'prev_page': page - 1 if start_of_page > 0 else None,
                'total_pages': all_pages,
                }
        return page_mapping
