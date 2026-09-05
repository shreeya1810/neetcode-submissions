class Solution:
    def rob(self, nums: List[int]) -> int:

        def recurse(i, memo={}):
            if i==len(nums)-1:
                return nums[i]
            if i==len(nums)-2:
                return max(nums[i], nums[i+1])
            if i in memo:
                return memo[i]
            memo[i]=max(recurse(i+1), recurse(i+2)+nums[i])
            return memo[i]
        return recurse(0, memo={})