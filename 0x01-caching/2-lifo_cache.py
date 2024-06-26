"""
Module implementing a LIFO caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache is a LIFO cache system that inherits from BaseCaching.

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

        if len(self.cache_data) > self.MAX_ITEMS:
            keys = list(self.cache_data.keys())
            self.cache_data.pop(keys[-2])
            print(f"DISCARD: {keys[-2]}")

    def get(self, key):
        """Get an item from the cache."""
        return self.cache_data.get(key, None)
