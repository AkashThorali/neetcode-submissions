class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        # get the dimensions of the grid
        rows = len(grid)
        cols = len(grid[0])

        # set to keep track of islands we've already visited
        visited = set()

        # count the number of islands
        islands = 0

        def bfs(r, c):
            q = deque([(r,c)])
            visited.add((r,c))
            while q:
                r, c = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for d in directions: 
                    row = r + d[0]
                    col = c + d[1]

                    # check if row and col are in bounds
                    # check if row and col are not already visited
                    # check if row and col equal an island (i.e. "1")
                    if (row in range(rows) and col in range(cols) and (row, col) not in visited and grid[row][col] == "1"):
                        q.append((row,col))
                        visited.add((row,col))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        return islands


        

        