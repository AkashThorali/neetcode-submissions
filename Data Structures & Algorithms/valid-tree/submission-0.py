class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        graph = defaultdict(list)
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        visited = set()

        def dfs(node):
            visited.add(node)
            for n1 in graph[node]:
                if n1 not in visited:
                    dfs(n1)

        dfs(0)
        return len(visited) == n
        