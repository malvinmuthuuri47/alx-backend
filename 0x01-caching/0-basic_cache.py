#!/usr/bin/env python3
"""
    A Python module that performs operations on a dictionary while
    depicting the usage of inheritance.
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
        The derived class that inherits from the BaseClass

        Args:
            BaseCaching: The BaseClass containing all the methods that
                         are being overridden
    """
    def put(self, key, item):
        """Add an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
        else:
            pass

    def get(self, key):
        """Get an item by key
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
