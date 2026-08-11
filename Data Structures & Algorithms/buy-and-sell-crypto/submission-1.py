class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two pointer approach 

        l = 0
        r = 1
        profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = max(profit , prices[r] - prices[l]) # sell - buy
            else:
                l = r
            r = r+1
        return profit
