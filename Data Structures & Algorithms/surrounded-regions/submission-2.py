class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len (board[0])

        def bfs(r,c):
            q = deque([(r,c)])
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            while q: 
                r, c = q.popleft()
                for d in directions: 
                    row = r + d[0]
                    col = c + d[1]
                    if (row in range(rows) and col in range(cols) and board[row][col] == "O"):
                        board[row][col] = "S"
                        q.append((row, col))


        for r in range(rows):
            for c in range(cols):
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    if board[r][c] == "O":
                        board[r][c] = "S"
                        bfs(r,c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "S":
                    board[r][c] = "O"
        