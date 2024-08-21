#!/usr/bin/env python3
""" class FIFOCache that inherits from BaseCaching and is a caching system"""

import queue
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    def __init__(self):
        """initializing"""
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """adding item to cache_data"""
        if key is None or item is None:
            return

        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data.items()) > self.MAX_ITEMS:
                cache_data_queue = queue.Queue()
                for key in self.cache_data.keys():
                    cache_data_queue.put(key)
                # first item name need to be removed
                fifo_key = cache_data_queue.get()
                dic_items = self.cache_data.items()
                print(f'DISCARD: {fifo_key}')
                self.cache_data = {key: value for key, value in dic_items
                               if key != fifo_key}

    def get(self, key):
        """gets item of given key"""
        if key is None or key not in self.cache_data.keys:
            return None
        return self.cache_data.get(key)
