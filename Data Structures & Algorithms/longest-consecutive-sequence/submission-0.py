class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0
        for num in nums:
            if num - 1 not in nums_set:
                length = 0
                c = num
                while c in nums_set:
                    length += 1
                    c += 1
                max_len = max(length, max_len)
        return max_len

