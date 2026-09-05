class Solution:
    def climbStairs(self, n: int) -> int:
    
        def climb(n, memo={}):
            if n==0:
                return 1
            if n<0:
                return 0
            if n in memo:
                return memo[n]
            memo[n]=climb(n-2)+climb(n-1)
            return memo[n]

        return climb(n, memo={})