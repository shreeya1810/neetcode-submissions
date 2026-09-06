class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for i in range(len(nums)):
            mapping[nums[i]] = i
        for i in range(len(nums)):
            if target - nums[i] in mapping:
                if i == mapping[target - nums[i]]:
                    continue
                if i < mapping[target-nums[i]]:
                    return [i, mapping[target-nums[i]]]
                return [mapping[target-nums[i]], i]
