class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        subsets = []
        def dfs(open_count, close_count):
            if len(subsets) == 2*n:
                res.append("".join(subsets))
                return
            
            # include open brackets
            if open_count < n:
                subsets.append("(")
                dfs(open_count + 1, close_count)
                subsets.pop()

            # include close brackets
            if close_count < open_count:
                subsets.append(")") 
                dfs(open_count, close_count + 1)
                subsets.pop()
            
        dfs(0, 0)
        return res

        