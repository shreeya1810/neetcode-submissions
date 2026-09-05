class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_set = set(nums)

        for n in nums:
            if target - n in nums_set:
                num1, num2 = n, target - n

        ans = []
        for i in range(len(nums)):
            if len(ans) == 2:
                return ans
            if nums[i] == num1:
                ans.append(i)
            elif nums[i] == num2:
                ans.append(i)
        
        return ans
            
                   