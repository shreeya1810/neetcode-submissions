class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1 or len(nums) == 2:
            return max(nums)
        
        max_rob = [0] * len(nums)
        max_rob[0], max_rob[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            max_rob[i] = max(max_rob[i - 2] + nums[i], max_rob[i - 1])

        return max_rob[-1] 