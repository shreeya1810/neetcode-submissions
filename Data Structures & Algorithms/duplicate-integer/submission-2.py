class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_nums = set()
        for n in nums:
            set_nums.add(n)
        return not(len(set_nums) == len(nums))
