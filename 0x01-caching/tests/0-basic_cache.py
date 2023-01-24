#!/usr/bin/env python3
"""
Module defines a class BasicCache that inherits from class BaseCache
and is a caching class
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    class is caching system inheriting the BaseCache

    Args::
        base_caching: class BaseCaching
    """

    def put(self, key, item):
        """
        assigns the item value for the key [key]
        """
        if key is None or item is None:
            pass
        self.cache_data[key] = item

    def get(self, key):
        """
        return the value in self.cache_data linked to key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
