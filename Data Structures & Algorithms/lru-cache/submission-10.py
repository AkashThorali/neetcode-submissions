from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.queue = deque([])
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key in self.cache.keys():
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache.keys():
            self.cache[key] = value
            self.queue.remove(key)
            self.queue.append(key)
        else: 
            self.cache[key] = value
            self.queue.append(key)
            if len(self.cache) > self.capacity:
                del self.cache[self.queue.popleft()]
        return None
        
