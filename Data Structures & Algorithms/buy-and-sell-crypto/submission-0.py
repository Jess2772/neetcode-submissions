class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]

        profit = 0
        for i in range (1, len(prices)):
            profit = max(profit, prices[i] - lowest)
            lowest = min(lowest, prices[i])

        return profit
