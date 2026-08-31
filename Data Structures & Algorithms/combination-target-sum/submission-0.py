class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []

        combination = []
        def dfs(index, total):
            if index >= len(nums):
                return
            if total == target:
                res.append(combination.copy())
                return
            if total > target:
                return

            # include nums[index]
            combination.append(nums[index])
            dfs(index, total + nums[index])
            combination.pop()

            # exclude nums[index]
            dfs(index + 1, total)

        dfs(0, 0)
        return res

        