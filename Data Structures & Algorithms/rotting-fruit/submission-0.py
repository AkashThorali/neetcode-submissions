class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid: 
            return -1
        
        # get the dimensions of the grid
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        q = deque()
        ones = 0

        # identify rotten fruit and number of fresh fruit
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1: 
                    ones += 1
        
        minutes = 0
        while q and ones > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for d in directions: 
                    row = r + d[0]
                    col = c + d[1]
                    if (row in range(rows) and col in range(cols) and grid[row][col] == 1):
                        grid[row][col] = 2
                        ones -= 1
                        q.append((row,col))
            minutes += 1
        
        if ones == 0:
            return minutes
        else: 
            return -1



        

        
        