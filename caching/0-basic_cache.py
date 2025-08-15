#!/usr/bin/python3
"""Basic caching module that stores items with no limit."""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache is a simple caching system with no size limit."""

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key: The key under which the item will be stored.
            item: The value to store in the cache.

        If either key or item is None, the method does nothing.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key: The key to look for in the cache.

        Returns:
            The value associated with the key, or None if the key is None
            or not found.
        """
        if key is None:
            return None
        return self.cache_data.get(key)
