class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: 
            return 0 
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        maxCount = 0
        
        def bfs(r,c):
            q = deque([(r,c)])
            visited.add((r,c))
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            count = 0
            while q:
                count += 1
                row, col = q.popleft()
                for d in directions: 
                    r = row + d[0]
                    c = col + d[1]
                    if (r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r,c) not in visited):
                        q.append((r,c))
                        visited.add((r,c))
            return count

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    maxCount = max(maxCount, bfs(r,c))
        
        return maxCount
        