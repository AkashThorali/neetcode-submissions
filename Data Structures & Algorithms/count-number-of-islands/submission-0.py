class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: 
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            q = deque([(r,c)])
            visited.add((r,c))
            directions = [[1, 0], [-1, 0], [0,1], [0,-1]]
            while q: 
                r,c = q.popleft()
                for d in directions: 
                    row = r + d[0]
                    col = c + d[1]
                    if (row in range(rows) and col in range(cols) and grid[row][col] == "1" and (row, col) not in visited): 
                        visited.add((row,col))
                        q.append((row,col))



        for r in range(rows): 
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        
        return islands

        