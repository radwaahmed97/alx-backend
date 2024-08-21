#!/usr/bin/env python3
"""class BasicCache that inherits from BaseCaching and is a caching system"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """BaseCaching class"""
    def __init__(self):
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """adding an item in the cache"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """getting an item by key"""
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
