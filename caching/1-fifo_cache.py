#!/usr/bin/python3
"""FIFO caching module.
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO cache system."""

    def __init__(self):
        """Initialize the FIFO cache."""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item to the cache."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            oldest_key = self.order.pop(0)
            del self.cache_data[oldest_key]
            print("DISCARD: {}".format(oldest_key))

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Get an item by key."""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
