"""
Module implementing a simple caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache is a simple cache system that inherits from BaseCaching.

    Methods:
    - put(key, item): Adds an item to the cache.
    - get(key): Retrieves an item from the cache.
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache."""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item from the cache."""
        return self.cache_data.get(key)
