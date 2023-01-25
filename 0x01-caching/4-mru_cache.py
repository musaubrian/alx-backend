#!/usr/bin/env python3
"""
Module defines a class MRUCache which is a caching system
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    defines a class MRUCache that inherits BaseCaching
    """

    def __init__(self):
        super().__init__()
        self.head, self.tail = "head", "tail"
        self.next, self.prev = {}, {}
        self.handle(self.head, self.tail)

    def handle(self, head, tail):
        """Handler function"""
        self.next[head], self.prev[tail] = tail, head

    def _remove(self, key):
        """Remove an element"""
        self.handle(self.prev[key], self.next[key])
        del self.prev[key], self.next[key], self.cache_data[key]

    def _add(self, key, item):
        """Adds a new element"""
        if len(self.cache_data) > BaseCaching.MAX_ITEMS - 1:
            print(f"DISCARD: {self.prev[self.tail]}")
            self._remove(self.prev[self.tail])

        self.cache_data[key] = item
        self.handle(self.prev[self.tail], key)
        self.handle(key, self.tail)

    def put(self, key, item):
        """
        assigns  the item value for the key self.cache_data[key]
        """
        if key and item:
            if key in self.cache_data:
                self._remove(key)
            self._add(key, item)

    def get(self, key):
        """
        returns the value in self.cache_data linked to key
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        if key in self.cache_data:
            val = self.cache_data[key]
            self._remove(key)
            self._add(key, val)

            return val
