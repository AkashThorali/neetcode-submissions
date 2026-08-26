class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []
        for i in nums: 
            if len(max_heap) < k: 
                heapq.heappush(max_heap, i)
            else:
                heapq.heappush(max_heap, i)
                heapq.heappop(max_heap)
        return max_heap[0]
        