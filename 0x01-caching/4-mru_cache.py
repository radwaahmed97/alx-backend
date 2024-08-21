#!/usr/bin/env python3
"""class MRUCache that inherits from BaseCaching and is a caching system"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """Most-recently-used caching replacment policy"""
    def __init__(self):
        """initializing"""
        self.stack_attitude = []
        super().__init__()

    def put(self, key, item):
        """adding item to cache_data"""
        if key and item:
            if self.cache_data.get(key):
                self.stack_attitude.remove(key)
            while len(self.stack_attitude) >= self.MAX_ITEMS:
                # Most-recently-used item name need to be removed
                lru_key = self.stack_attitude.pop()
                self.cache_data.pop(lru_key)
                print(f'DISCARD: {lru_key}')
            self.stack_attitude.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """gets item of given key"""
        if self.cache_data.get(key):
            self.stack_attitude.remove(key)
            self.stack_attitude.append(key)
        return self.cache_data.get(key)
