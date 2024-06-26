"""
Module implementing a MRU caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache is a MRU cache system that inherits from BaseCaching.

    Methods:
    - put(key, item): Adds an item to the cache.
    - get(key): Retrieves an item from the cache.
    """

    def __init__(self):
        super().__init__()
        self.track = {}
        self.count = 0

    def put(self, key, item):
        """Add an item in the cache."""
        if key and item:
            self.count += 1
            self.track[key] = self.count
            self.cache_data[key] = item

            if len(self.cache_data) > self.MAX_ITEMS:
                track = sorted(self.track, key=lambda k: self.track[k])
                self.track.pop(track[-2])
                self.cache_data.pop(track[-2])
                print(f"DISCARD: {track[-2]}")

    def get(self, key):
        """Get an item from the cache."""
        print(f"{key} is been operated on")
        self.count += 1
        if key in self.cache_data:
            self.track[key] = self.count
        return self.cache_data.get(key, None)
