class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for index, point in enumerate(points): 
            x,y = point
            distance = math.sqrt((x**2) + (y**2))
            heapq.heappush(max_heap, [-distance, index])
            if len(max_heap) > k: 
                heapq.heappop(max_heap)

        res = []
        for i in max_heap: 
            res.append(points[i[1]])
        return res