from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minmum = prices[0]

        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - minmum)
            minmum = min(minmum, prices[i])
        return profit