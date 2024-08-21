#!/usr/bin/env python3
"""class LFUCache that inherits from BaseCaching and is a caching system"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """Least frequently used caching replacment policy"""
    def __init__(self):
        """initializing"""
        self.lfu = {}
        self.toqueue = []
        super().__init__()

    def put(self, key, item):
        """adding item to cache_data"""
        if key and item:
            if (len(self.toqueue) >= self.MAX_ITEMS and
                    not self.cache_data.get(key)):
                lfu_key = self.toqueue.pop(0)
                self.lfu.pop(lfu_key)
                self.cache_data.pop(lfu_key)
                print('DISCARD: {}'.format(lfu_key))

            if self.cache_data.get(key):
                self.toqueue.remove(key)
                self.lfu[key] += 1
            else:
                self.lfu[key] = 0

            use_index = 0
            while (use_index < len(self.toqueue) and
                   not self.lfu[self.toqueue[use_index]]):
                use_index += 1
            self.toqueue.insert(use_index, key)
            self.cache_data[key] = item

    def get(self, key):
        """gets item of given key"""
        if self.cache_data.get(key):
            self.lfu[key] += 1
            if self.toqueue.index(key) + 1 != len(self.toqueue):
                while (self.toqueue.index(key) + 1 < len(self.toqueue) and
                       self.lfu[key] >=
                       self.lfu[self.toqueue[self.toqueue.index(key) + 1]]):
                    location_item = self.toqueue.index(key) + 1
                    popped_item = self.toqueue.pop(self.toqueue.index(key))
                    self.toqueue.insert(location_item, popped_item)
        return self.cache_data.get(key)
