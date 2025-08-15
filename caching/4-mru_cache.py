#!/usr/bin/python3
"""
MRU Cache Module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache class inherits from BaseCaching and implements MRU policy."""

    def __init__(self):
        """Initialize the MRUCache."""
        super().__init__()

    def put(self, key, item):
        """Add an item to the cache and discard MRU if full."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            del self.cache_data[key]  # Remove first to update usage

        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Most recently used is the last inserted item
            mru_key = next(reversed(self.cache_data))
            del self.cache_data[mru_key]
            print("DISCARD: {}".format(mru_key))

        self.cache_data[key] = item  # Insert at the end (most recently used)

    def get(self, key):
        """Retrieve an item from the cache."""
        if key is None or key not in self.cache_data:
            return None

        item = self.cache_data[key]
        del self.cache_data[key]  # Remove and re-insert to update order
        self.cache_data[key] = item
        return item
