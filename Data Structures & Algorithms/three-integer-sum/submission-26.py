class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        duplicates = set()
        res = []

        for i in range(len(nums) - 1):
            l = i + 1
            r = len(nums) - 1
            while l < r:

                # sum is greater than zero, choose a smaller number
                if nums[l] + nums[i] + nums[r] > 0:
                    r -= 1
                
                # sum is less than zero, choose a bigger number
                elif nums[l] + nums[i] + nums[r] < 0:
                    l += 1
                else:
                    duplicates.add((nums[i], nums[l], nums[r])) 
                    while l < r and nums[l + 1] == nums[l]:
                        l += 1
                    while l < r and nums[r - 1] == nums[r]:
                        r -= 1
                    l += 1
                    r -= 1
        
        for a,b,c in duplicates:
            res.append([a,b,c])
        return res
        