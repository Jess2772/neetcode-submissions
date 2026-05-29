class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)

        dp[0] = 0

        for money in range (1, amount + 1):
            for c in coins:
                if c <= money:
                    dp[money] = min(dp[money], dp[money - c] + 1)
        
        return dp[-1] if dp[-1] != float('inf') else -1

                    

