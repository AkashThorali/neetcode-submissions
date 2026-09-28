class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        q = deque()
        land_cell = 0
        land_val = (2 ** 31) - 1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                if grid[r][c] == land_val: 
                    land_cell += 1
            
        count = 1
        while q: 
            directions = [[1,0], [-1,0], [0,1], [0, -1]]
            for _ in range(len(q)):
                r, c = q.popleft()
                for d in directions: 
                    row = d[0] + r
                    col = d[1] + c
                    if (row in range(rows) and col in range(cols) and grid[row][col] == land_val): 
                        grid[row][col] = count
                        q.append((row, col))
                        land_cell -= 1
            count += 1

                
                
                

        
        