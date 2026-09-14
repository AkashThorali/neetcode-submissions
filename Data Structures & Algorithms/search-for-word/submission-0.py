class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # grab the dimensions of the board

        ROW = len(board)
        COL = len(board[0])
        path = set()

        def dfs(row, col, index):
            if index == len(word):
                return True
            if (row < 0 or col < 0 or row >= ROW or col >= COL): 
                return
            if (word[index] != board[row][col] or (row, col) in path):
                return
            
            path.add((row, col))
            res = (dfs(row + 1, col, index + 1) or dfs(row - 1, col, index + 1) or dfs(row, col + 1, index + 1) or dfs(row, col - 1, index + 1))
            path.remove((row,col))
            return res

        
        for r in range(ROW):
            for c in range(COL): 
                if dfs(r,c,0):
                    return True
        return False
            

        