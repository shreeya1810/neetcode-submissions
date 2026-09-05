class Solution:
    def rob(self, nums: List[int]) -> int:

        rob = [0] * (len(nums) + 1)
        rob[0], rob[1] = 0, nums[0]

        for i in range(2, len(nums) + 1):
            rob[i] = max(nums[i-1] + rob[i-2], rob[i-1])

        return rob[-1]