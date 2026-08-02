class LRUCache:

    def __init__(self, capacity: int):
        self.res = []
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        temp = -1
        for i in range(len(self.res)):
            if self.res[i][0] == key: 
                temp = self.res[i][1]
                self.res.pop(i)
                self.res.append([key, temp])
                break
        return temp
        
    def put(self, key: int, value: int) -> None:
        for i in range(len(self.res)):
            if self.res[i][0] == key:
                self.res.pop(i)
                break
        self.res.append([key, value])
        if len(self.res) > self.capacity: 
            del self.res[0]

        
