class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def backtrack(currAmt, memo):
            if currAmt == 0:
                return 0
            if currAmt < 0:
                return float('inf')
            if currAmt in memo:
                return memo[currAmt]

            min_coins = float('inf')
            for coin in coins:
                num_coins = backtrack(currAmt - coin, memo)
                # if num_coins != float('inf'):
                min_coins = min(min_coins, num_coins + 1)

            memo[currAmt] = min_coins
            return memo[currAmt]

        result = backtrack(amount, {})
        return result if result != float('inf') else -1
