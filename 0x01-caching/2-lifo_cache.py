#!/usr/bin/env python3
"""LIFO Caching"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
        Derive class inheriting methods and attributes of the BaseCaching
        class
    """
    def __init__(self):
        """
            Construtor function that calls the superclass constructor
            to initialize varibales such as the caching system(dict)
            The constructor also initializes a list that will be used
            to preserve the order of insertion of the keys into the
            caching dictionary
        """
        super().__init__()
        self.cache_data = {}  # Dict to store cached items
        self.key_order = []  # Stack to keep track of insertion order

    def put(self, key, item):
        """
            This method adds the key to the caching system by checking
            if the cache is free. If it's not, a pop occurs of the last
            element to be added in the cache to create space to add the
            new key whose value is item

            Args:
                key - The key of the caching system
                item - Value of the caching system
        """
        if key is None or item is None:
            return
        else:
            self.cache_data[key] = item
            self.key_order.append(key)

            if len(self.cache_data) > self.MAX_ITEMS:
                lst_idx = self.key_order.pop(-2)
                del self.cache_data[lst_idx]
                print(f"DISCARD {lst_idx}")

    def get(self, key):
        """
            This function returns the value of the key passed to it
            provided the key is present in the cache and its not None
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
