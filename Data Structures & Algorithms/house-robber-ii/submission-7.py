class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1:
            return max(nums)
        nums1 = nums[:-1]
        nums2 = nums[1:]

        rob1 = [0] * (len(nums1) + 1)
        rob1[0], rob1[1] = 0, nums1[0]

        for i in range(2, len(nums1) + 1):
            rob1[i] = max(nums1[i-1] + rob1[i-2], rob1[i-1])

        rob2 = [0] * (len(nums2) + 1)
        rob2[0], rob2[1] = 0, nums2[0]

        for i in range(2, len(nums2) + 1):
            rob2[i] = max(nums2[i-1] + rob2[i-2], rob2[i-1])

        return max(rob1[-1], rob2[-1])
        