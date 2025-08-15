#!/usr/bin/python3
"""
LRU Cache Module
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class inherits from BaseCaching.
    """

    def __init__(self):
        """
        Initialize the LRUCache instance.
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            del self.cache_data[key]  # Remove first to update its order

        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            oldest_key = next(iter(self.cache_data))  # LRU key
            del self.cache_data[oldest_key]
            print("DISCARD: {}".format(oldest_key))

        self.cache_data[key] = item  # Insert at the end (most recently used)

    def get(self, key):
        """
        Retrieve an item from the cache.

        """
        if key is None or key not in self.cache_data:
            return None

        item = self.cache_data[key]
        del self.cache_data[key]  # Remove and re-insert to update order
        self.cache_data[key] = item
        return item
