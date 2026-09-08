class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for k in range(len(nums) - 2):
            if nums[k] > 0:
                break # smallest number is +ve so the sum can't be 0
            target = -nums[k]
            if k != 0 and nums[k - 1] == nums[k]:
                continue
            i, j = k + 1, len(nums) - 1
            while i < j:
                curr = nums[i] + nums[j]
                if curr > target:
                    j -= 1
                elif curr < target:
                    i += 1
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
        return res