#!/usr/bin/env python3
"""
module implements a simple pagination
"""
import csv
import math
from typing import Dict, List


def index_range(page: int, page_size) -> tuple:
    """
    Returns a tuple  containing a start index and an end index

    Args::
        page(int)
        page_size(int)
    """
    indices = page_size * (page - 1), page * page_size
    return indices


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
        Use assert to verify that both args are ints greater than 0.
        Use index_range to find the correct indexes to paginate the dataset
        If the input arguments are out of range for the dataset,
            an empty list should be returned.
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        indices = index_range(page, page_size)

        try:
            data = self.dataset()
            return (data[indices[0]: indices[1]])
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        returns a dictionary
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        result_dict = {
                "page_size": len(data),
                "page": page,
                "date": data,
                "next_page": next_page,
                "prev_page": prev_page,
                "total_pages": total_pages
                }

        return result_dict
