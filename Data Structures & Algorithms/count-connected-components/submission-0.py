class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
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

        count = 0
        for i in range(n):
            if i in visited: 
                continue
            else:
                dfs(i)
                count += 1
        return count

        