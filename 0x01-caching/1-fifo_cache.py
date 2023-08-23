#!/usr/bin/env python3
"""FIFO CACHING"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """Child class inheriting from BaseCaching Parent class"""
    def __init__(self):
        """
        Call the super __init__ to initialize the cache_data which
        is the caching system
        Create an initialize a List that will be used to store the keys
        entered into the dictionary in insertion order
        """
        super().__init__()
        self.cache_data = {}
        self.key_order = []

    def put(self, key, item):
        """
            This function adds new values to the caching system and tests
            to ensure that the FIFO Caching is followed when adding new
            items to the dict. If the cache is full, then the Oldest
            element is popped off the cache to create room for the new
            element.

            Args:
                key - the key to be stored in the cache
                item - the value of the key to be stored
        """
        if key is None and item is None:
            return
        else:
            self.cache_data[key] = item
            self.key_order.append(key)

            if len(self.cache_data) > self.MAX_ITEMS:
                oldest_key = self.key_order.pop(0)
                del self.cache_data[oldest_key]
                print(f"DISCARD {oldest_key}")

    def get(self, key):
        """This function gets the value of the key passed to it"""
        if key is None or key not in self.key_order:
            return None
        return self.cache_data[key]
