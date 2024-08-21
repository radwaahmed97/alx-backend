#!/usr/bin/env python3
""" class FIFOCache that inherits from BaseCaching and is a caching system"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    def __init__(self):
        """initializing"""
        super().__init__()
        self.cache_data = {}
        self.toqueue = []

    def put(self, key, item):
        """adding item to cache_data"""
        if key and item:
            if self.cache_data.get(key):
                self.toqueue.remove(key)
            self.toqueue.append(key)
            self.cache_data[key] = item
            if len(self.toqueue) > BaseCaching.MAX_ITEMS:
                # first item name need to be removed
                fifo_key = self.toqueue.pop(0)
                self.cache_data.pop(fifo_key)
                print(f'DISCARD: {fifo_key}')

    def get(self, key):
        """gets item of given key"""
        return self.cache_data.get(key)
