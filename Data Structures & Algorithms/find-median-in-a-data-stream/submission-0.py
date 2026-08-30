class MedianFinder:

    def __init__(self):
        self.median = []

    def addNum(self, num: int) -> None:
        self.median.append(num)
    
    def findMedian(self) -> float:
        self.median.sort()
        if len(self.median) % 2 == 1:
            return self.median[len(self.median) // 2]
        else: 
            compute = (self.median[len(self.median) // 2] + self.median[(len(self.median) // 2) - 1]) / 2
            return compute

        
        