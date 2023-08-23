#!/usr/bin/env python3
"""MRU Caching"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    Child class that inherits properties and methods of the Base class
    and initializes them
    Call the super class constructor to initialize the cache system and
    implement a counter that will be used to determine the age of the
    elements in the cache
    """
    def __init__(self):
        """
        Initialize the instance of the class with the age bit and counter
        to track the age of the instance of the class in the cache
        """
        super().__init__()
        self.age_bits = {}
        self.counter = 0

    def put(self, key, value):
        """
        This function adds a new element to the cache and updates it
        age bit. If the element is already present in the cache, the age
        isn't updated.

        Args:
            key - The key to store in the cache
            value - The value asscosiated with the given key
        """
        if key or item:
            if key in self.cache_data:
                # When updatig an existing key's value, do not update its age
                self.cache_data[key] = value
            elif len(self.cache_data) >= self.MAX_ITEMS:
                # Find the most recently used item based on age bits
                mru_key = max(self.age_bits, key=self.age_bits.get)
                del self.cache_data[mru_key]
                del self.age_bits[mru_key]
                print(f"DISCARD {mru_key}")

            # Add the new key-value to the cache with the current counter val
            self.cache_data[key] = value
            self.age_bits[key] = self.counter
        else:
            return

    def get(self, key):
        """This function gets the key from the cache"""
        if key is None or key not in self.cache_data:
            return None
        else:
            if key in self.cache_data:
                # Update the counter and age bits for the accessed item
                self.counter += 1
                self.age_bits[key] = self.counter
                return self.cache_data[key]
