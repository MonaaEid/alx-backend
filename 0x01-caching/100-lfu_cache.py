#!/usr/bin/env python3
"""LFU Caching"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFUCache defines:
      - caching system
    """

    def __init__(self):
        """Initiliaze
        """
        super().__init__()
        self.queue = []
        self.frequency = {}
    
    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.frequency[key] += 1
                self.queue.remove(key)
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    discard = self.queue.pop(0)
                    del self.cache_data[discard]
                    del self.frequency[discard]
                    print("DISCARD:", discard)
                self.cache_data[key] = item
                self.frequency[key] = 1
            self.queue.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data:
            self.frequency[key] += 1
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data[key]
        return None
