class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        l, r = 0, 1

        while r < len(prices):
            while r < len(prices) and prices[r] - prices[l] < 0:
                l = r
                r += 1
            print(l, r)
            if r < len(prices):
                max_profit = max(max_profit, prices[r]-prices[l])
                r += 1
            
        return max_profit
        