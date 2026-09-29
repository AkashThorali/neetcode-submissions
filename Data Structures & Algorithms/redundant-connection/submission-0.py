class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        par = [i for i in range(n+1)]
        rank = [1] * (n+1)

        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        def union(n1, n2):
            n1, n2 = find(n1), find(n2)
            if n1 == n2: 
                return False
            
            if rank[n1] < rank[n2]:
                n1, n2 = n2, n1
            par[n2] = n1
            rank[n1] += n2
            return True
        

        for n1, n2 in edges: 
            if not union(n1, n2):
                return [n1, n2]
        