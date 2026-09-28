class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # get the dimensions of the grid
        rows = len(heights)
        cols = len(heights[0])

        pacific = deque()
        atlantic = deque()
        
        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0: 
                    pacific.append((r, c))
                if r == rows - 1 or c == cols - 1:
                    atlantic.append((r, c))

        directions = [[1,0], [-1,0], [0, 1], [0, -1]]

        visited_p = set()
        while pacific:
            for _ in range(len(pacific)):
                r,c = pacific.popleft()
                visited_p.add((r,c))
                for d in directions: 
                    row = d[0] + r
                    col = d[1] + c
                    if (row in range(rows) and col in range(cols) and heights[row][col] >= heights[r][c] and (row, col) not in visited_p):
                        pacific.append((row,col)) 
        
        visited_a = set()
        while atlantic:
            for _ in range(len(atlantic)):
                r,c = atlantic.popleft()
                visited_a.add((r,c))
                for d in directions: 
                    row = d[0] + r
                    col = d[1] + c
                    if (row in range(rows) and col in range(cols) and heights[row][col] >= heights[r][c] and (row, col) not in visited_a):
                        atlantic.append((row,col))
        
        return list(visited_p & visited_a)
            
        
                
                


        