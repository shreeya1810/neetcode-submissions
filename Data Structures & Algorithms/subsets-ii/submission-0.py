class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        # res = set()
        # def backtrack(i = 0, curr = []):
        #     if i == len(nums):
        #         res.add(tuple(curr))
        #         return
        #     backtrack(i + 1, curr)
        #     backtrack(i + 1, curr + [nums[i]])
        # backtrack(0, [])
        # return [list(subset) for subset in res]

        nums.sort()
        res = []

        def backtrack(i = 0, curr = []):
            if i == len(nums):
                res.append(curr.copy())
                return
            backtrack(i + 1, curr + [nums[i]])
            while i + 1 < len(nums) and nums[i + 1] == nums[i] :
                i += 1
            backtrack(i + 1, curr)
        backtrack(0, [])
        return res


