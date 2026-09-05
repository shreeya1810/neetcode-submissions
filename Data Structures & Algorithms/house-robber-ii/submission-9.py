class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums)
        
        # Helper function to rob a linear sequence of houses
        def rob_linear(houses):
            n = len(houses)
            if n == 1:
                return houses[0]
            if n == 2:
                return max(houses)
            
            max_rob = [0] * n
            max_rob[0], max_rob[1] = houses[0], max(houses[0], houses[1])
            
            for i in range(2, n):
                max_rob[i] = max(max_rob[i - 2] + houses[i], max_rob[i - 1])
            
            return max_rob[-1]
        
        # Rob from the first house to the second-last house
        rob_first_to_second_last = rob_linear(nums[:-1])
        # Rob from the second house to the last house
        rob_second_to_last = rob_linear(nums[1:])
        
        return max(rob_first_to_second_last, rob_second_to_last)
