class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(curr = [], used = set()):
            if len(curr) == len(nums):
                res.append(curr[:])
            for num in nums:
                if num not in used:
                    curr.append(num)
                    used.add(num)
                    backtrack(curr, used)
                    curr.pop()
                    used.remove(num)
        backtrack([], set())
        return res