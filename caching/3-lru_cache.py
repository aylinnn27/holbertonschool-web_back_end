#!/usr/bin/python3
"""
LRU Cache Module
Defines a caching system that follows the Least Recently Used (LRU) policy.
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class inherits from BaseCaching.

    Implements a caching system with the Least Recently Used (LRU) eviction policy.
    When the cache exceeds its maximum size, the least recently used item is discarded.

    Attributes:
        cache_data (dict): Inherited from BaseCaching, stores cached items.
    """

    def __init__(self):
        """
        Initialize the LRUCache instance.

        Calls the parent class constructor to initialize cache_data.
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache.

        If the key already exists, update its value and mark it as recently used.
        If the cache exceeds its maximum size, remove the least recently used item.

        Args:
            key (str): The key for the cache entry.
            item (any): The value to store in the cache.

        Returns:
            None
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

        Marks the item as recently used by moving it to the end.

        Args:
            key (str): The key of the cache entry.

        Returns:
            any: The value associated with the key, or None if key is not found.
        """
        if key is None or key not in self.cache_data:
            return None

        item = self.cache_data[key]
        del self.cache_data[key]  # Remove and re-insert to update order
        self.cache_data[key] = item
        return item
