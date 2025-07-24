# 24 Jul


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxi = -1
        profit = -1
        for i in range(len(prices)-1, -1, -1):
            maxi = max(maxi, prices[i])
            profit = max(profit, maxi - prices[i])
        return profit