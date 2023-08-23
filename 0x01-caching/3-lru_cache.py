#!/usr/bin/env python3
"""This module implements the LRU Caching"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    This class calls the parent constructor to initialize the caching
    mechanism and also initializes the age_bits dict for storing the
    age of each element in the cache and a counter to be used on each
    element to update the age_bits value every time an element is
    inserted into the cache and the cache is full
    """
    def __init__(self):
        super().__init__()
        self.age_bits = {}
        self.counter = 0

    def put(self, key, value):
        """
        This function adds a new key to the cache. If the cache is full,
        the key with the smallest age_bit gets removed from the cache to
        create room for the new element.
        The elements that exist in the cache won't have their ages updated

        Args:
            key - The key
            value - The value for the key
        """
        self.counter += 1
        if key in self.cache_data:
            # When updating an existing key's value, do not update its age
            self.cache_data[key] = value
        elif len(self.cache_data) >= self.MAX_ITEMS:
            # Find the least recently used item based on age bits
            lru_key = min(self.age_bits, key=self.age_bits.get)
            del self.cache_data[lru_key]
            del self.age_bits[lru_key]
            print(f"DISCARD {lru_key}")

        # Add the new key-value pair to the cache with the current counter val
        self.cache_data[key] = value
        self.age_bits[key] = self.counter

    def get(self, key):
        """This function gets the values present in the cache system"""
        if key is None or key not in self.cache_data:
            return None
        else:
            self.counter += 1
            self.age_bits[key] = self.counter
            return self.cache_data[key]
