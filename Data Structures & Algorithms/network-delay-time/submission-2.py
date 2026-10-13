class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        network = defaultdict(list)
        for source, target, weight in times:
            network[source].append((weight, target))

        minHeap = [(0, k)]
        visit = set()
        t = 0

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)

            t = max(t, w1)

            for w2, n2 in network[n1]:
                heapq.heappush(minHeap, ((w1 + w2), n2))
        return t if len(visit) == n else -1
        