class Solution:
    def rob(self, nums: List[int]) -> int:

        def recurse(nums, i, memo={}):
            if i==len(nums)-1:
                return nums[i]
            if i==len(nums)-2:
                return max(nums[i], nums[i+1])
            if i in memo:
                return memo[i]
            memo[i]=max(recurse(nums, i+1, memo), recurse(nums, i+2, memo)+nums[i])
            return memo[i]
        if len(nums) == 1:
            return nums[0]
        return max(recurse(nums[:-1], 0, memo={}), recurse(nums[1:], 0, memo={}))