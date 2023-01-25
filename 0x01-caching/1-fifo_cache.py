#!/usr/bin/env python3
"""
Module defines a class FIFOCache that inherits from BaseCaching
and is a caching system
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    defines a class FIFOCaching which inherits BaseCaching

    Args::
        BaseCaching: class being inherited
    """

    def put(self, key, item):
        """
        assigns  the item value for the key self.cache_data[key]
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # sort the dictionary
            sorted_dict = sorted(self.cache_data)

            key_to_remove = sorted_dict[0]
            self.cache_data.pop(key_to_remove)
            print(f"DISCARD: {key_to_remove}")

    def get(self, key):
        """
        returns the value in self.cache_data linked to key
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data.get(key)
