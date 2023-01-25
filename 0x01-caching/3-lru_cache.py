#!/usr/bin/env python3
"""
Module defines a class LRUCache that inherits from BaseCaching
and is a caching system:
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    defines class LRUCache
    """

    def __init__(self):
        super().__init__()
        self.head, self.tail = "-", "="
        self.next, self.prev = {}, {}
        self.handle(self.head, self.tail)

    def handle(self, head, tail):
        """
        handler function
        """
        self.next[head], self.prev[tail] = tail, head

    def _remove(self, key):
        """
        removes an item
        """
        self.handle(self.prev[key], self.next[key])
        del self.prev[key], self.next[key], self.cache_data[key]

    def _add(self, key, item):
        """
        adds an item
        """
        self.cache_data[key] = item
        self.handle(self.prev[self.tail], key)
        self.handle(key, self.tail)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print(f"DISCARD: {self.next[self.head]}")
            self._remove(self.next[self.head])

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
