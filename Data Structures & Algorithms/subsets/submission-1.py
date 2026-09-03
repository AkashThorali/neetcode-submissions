class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []

        subsets = []
        def dfs(index):
            if index == len(nums):
                return

            subsets.append(nums[index])
            res.append(subsets.copy())
            dfs(index + 1)
            subsets.pop()

            dfs(index + 1)

        dfs(0)
        res.append([])
        return res
        