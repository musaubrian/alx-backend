#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List


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
        """
        Use assert to verify that index is in a valid range.
        If the user queries index 0, page_size 10,
            they will get rows indexed 0 to 9 included.
        If they request the next index (10) with page_size 10, but
            rows 3, 6 and 7 were deleted,
            the user should still receive rows indexed 10 to 19 included.
        """
        dataset = self.indexed_dataset()

        assert type(index) is int and index < len(dataset)
        assert type(page_size) is int and page_size > 0

        data = []
        idx, next_idx = index, index + page_size

        while idx < next_idx:
            if idx in dataset.keys():
                data.append(dataset[idx])
            else:
                next_idx += 1
            idx += 1

        result_dict = {
                "index": index,
                "next_index": next_idx,
                "page_size": page_size,
                "data": len(data)
                }
        return result_dict
