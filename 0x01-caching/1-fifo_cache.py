"""
Module implementing a FIFO caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache is a FIFO cache system that inherits from BaseCaching.

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
            self.cache_data.pop(keys[0])
            print(f"DISCARD: {keys[0]}")

    def get(self, key):
        """Get an item from the cache."""
        return self.cache_data.get(key, None)
