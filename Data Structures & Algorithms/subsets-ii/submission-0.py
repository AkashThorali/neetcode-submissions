class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        res = [[]]
        subsets = []
        def dfs(index):
            if index == len(nums):
                return
            
            # include value at index
            subsets.append(nums[index])
            res.append(subsets.copy())
            dfs(index + 1)

            # move to the next index
            subsets.pop()
            while index + 1 < len(nums) and nums[index + 1] == nums[index]:
                index += 1
            dfs(index + 1)

        dfs(0)
        return res