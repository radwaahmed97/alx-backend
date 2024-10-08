#!/usr/bin/env python3
"""class LIFOCache that inherits from BaseCaching and is a caching system"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """last in first out caching replacment policy"""
    def __init__(self):
        """initializing"""
        self.toqueue = []
        super().__init__()

    def put(self, key, item):
        """adding item to cache_data"""
        if key and item:
            if self.cache_data.get(key):
                self.toqueue.remove(key)
            self.toqueue.append(key)
            self.cache_data[key] = item
            if len(self.toqueue) > self.MAX_ITEMS:
                # last item name need to be removed
                lifo_key = self.toqueue.pop(len(self.toqueue) - 2)
                self.cache_data.pop(lifo_key)
                print(f'DISCARD: {lifo_key}')

    def get(self, key):
        """gets item of given key"""
        return self.cache_data.get(key)
