#!/usr/bin/python3
"""LIFO caching module"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching system"""

    def __init__(self):
        """Initialize the LIFO cache"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = self.order.pop()
            del self.cache_data[last_key]
            print("DISCARD: {}".format(last_key))

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Retrieve an item from the cache"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
