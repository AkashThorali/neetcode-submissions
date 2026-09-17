class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        palindrome = []
        def dfs(index):
            if index == len(s):
                res.append(palindrome.copy())
                return
            
            for end in range(index + 1, len(s) + 1):
                substring = s[index:end]
                if substring == substring[::-1]:
                    palindrome.append(substring)
                    dfs(end)
                    palindrome.pop()
        
        dfs(0)
        return res
        