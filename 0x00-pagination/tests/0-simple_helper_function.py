#!/usr/bin/env python3
"""
Return a tuple of size two containing a start index
and an end index corresponding to the range of indexes to return in a list
"""


def index_range(page: int, page_size) -> tuple:
    """
    Returns a tuple  containing a start index and an end index

    Args::
        page(int)
        page_size(int)
    """
    indices = page_size * (page - 1), page * page_size
    return indices
