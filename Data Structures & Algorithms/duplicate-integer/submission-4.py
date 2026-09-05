class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        array_set = set(nums)
        if len(list(array_set)) < len(nums):
            return True
        return False

