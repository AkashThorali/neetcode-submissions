class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows = len(heights)
        cols = len(heights[0])

        pacific = deque()
        atlantic = deque()

        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0:
                    pacific.append((r,c))
                if r == rows - 1 or c == cols - 1:
                    atlantic.append((r,c))
        
        visited_p = set()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        while pacific:
            for _ in range(len(pacific)):
                row, col = pacific.popleft()
                visited_p.add((row,col))
                for d in directions:
                    r = row + d[0]
                    c = col + d[1]
                    if (r in range(rows) and c in range(cols) and (r,c) not in visited_p and heights[r][c] >= heights[row][col]):
                        pacific.append((r,c))

        visited_a = set()
        while atlantic:
            for _ in range(len(atlantic)):
                row, col = atlantic.popleft()
                visited_a.add((row,col))
                for d in directions:
                    r = row + d[0]
                    c = col + d[1]
                    if (r in range(rows) and c in range(cols) and (r,c) not in visited_a and heights[r][c] >= heights[row][col]):
                        atlantic.append((r,c))
        
        return list(visited_p & visited_a)
            
        