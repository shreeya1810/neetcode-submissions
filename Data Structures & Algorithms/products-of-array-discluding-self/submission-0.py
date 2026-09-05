from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # before[i] = product of all elements before index i
        before = []
        for i in range(n):
            if i == 0:
                before.append(1)
            else:
                before.append(nums[i - 1] * before[i - 1])

        # after[i] = product of all elements after index i
        after = [1] * n
        for i in range(n - 2, -1, -1):
            after[i] = after[i + 1] * nums[i + 1]

        # combine element-wise
        return [before[i] * after[i] for i in range(n)]