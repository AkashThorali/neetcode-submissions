class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        combination = []

        def dfs(index, total):
            if total == target:
                res.append(combination.copy())
                return
            if total > target or index == len(candidates):
                return
            
            # includes candidates[index]
            combination.append(candidates[index])
            dfs(index + 1, total + candidates[index])
            combination.pop()

            # process next element
            while index + 1 < len(candidates) and candidates[index] == candidates[index+1]:
                index += 1
            dfs(index + 1, total)
   
        dfs(0, 0)
        return res