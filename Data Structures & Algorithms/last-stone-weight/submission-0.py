class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for i in stones: 
            heapq.heappush(max_heap, -i)
        
        while len(max_heap) > 1:
            x = -heapq.heappop(max_heap)
            y = -heapq.heappop(max_heap)
            if x > y: 
                diff = x - y
                heapq.heappush(max_heap, -diff)
        if not max_heap:
            return 0
        else: 
            return abs(max_heap[0])