from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity=3):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return None
        self.cache.move_to_end(key, last=False)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key, last=False)
        else:
            self.cache[key] = value
            self.cache.move_to_end(key, last=False)

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=True)

    def list_cache(self):
        return list(self.cache.keys())
