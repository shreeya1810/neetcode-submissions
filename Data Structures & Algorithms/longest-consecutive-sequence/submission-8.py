class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_set = set(nums)
        starts = {}
        for n in num_set:
            if n - 1 not in num_set:
                starts[n] = 1
        for start in starts:
            curr = start + 1
            while curr in num_set:
                starts[start] += 1
                curr += 1
        return max(starts.values())