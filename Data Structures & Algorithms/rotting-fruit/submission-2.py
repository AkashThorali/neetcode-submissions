class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        q = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2: 
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        minutes = 0
        visited = set()
        while q and fresh > 0: 
            minutes += 1 
            for _ in range(len(q)):
                r, c = q.popleft()
                directions = [[1,0], [0,1], [-1,0], [0,-1]]
                for d in directions: 
                    row = r + d[0]
                    col = c + d[1]
                    if (row in range(rows) and col in range(cols) and grid[row][col] == 1 and (row, col) not in visited):
                        q.append((row,col))
                        visited.add((row,col))
                        fresh -= 1
        if fresh != 0:
            return -1
        return minutes


                


    

        