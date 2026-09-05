from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)
        
        # Step 1: Calculate maxLeft
        maxLeft = [0] * n
        maxLeft[0] = height[0]
        for i in range(1, n):
            maxLeft[i] = max(maxLeft[i-1], height[i])
        
        # Step 2: Calculate maxRight
        maxRight = [0] * n
        maxRight[-1] = height[-1]
        for i in range(n-2, -1, -1):
            maxRight[i] = max(maxRight[i+1], height[i])
        
        # Step 3: Calculate trapped water
        water = 0
        for i in range(n):
            water += min(maxLeft[i], maxRight[i]) - height[i]
        
        return water