class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, curr_sum, curr):
            if i == len(nums):
                return
            if curr_sum > target:
                return
            if curr_sum == target:
                res.append(curr)
                return
            backtrack(i, curr_sum + nums[i], curr + [nums[i]])
            backtrack(i + 1, curr_sum, curr)
        
        backtrack(0, 0, [])
        return res