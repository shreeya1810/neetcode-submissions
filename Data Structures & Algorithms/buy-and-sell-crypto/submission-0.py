class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buying=prices[0]
        max_profit=0
        i=1
        for i in range(0, len(prices)):
            if prices[i]-buying>max_profit:
                max_profit=prices[i]-buying
            if buying>prices[i]:
                buying=prices[i]
        return max_profit
