#!/usr/bin/env python3
"""
Module defines a class LIFOCache that inherits from BaseCaching 
and is a caching system
"""
from types import NoneType
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    defines a class LIFOCache
    """

    def __init__(self):
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        assigns the item value for the key [key]
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            del self.cache_data[self.keys[-1]]
            print(f"DISCARD: {self.keys[-1]}")
        self.keys.append(key)

    def get(self, key):
        """
        return the value in self.cache_data linked to key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
