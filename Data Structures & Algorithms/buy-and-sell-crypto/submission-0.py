class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_min=float("inf")
        max_profit=0
        for right, price in enumerate(prices):
            max_profit=max(max_profit,price-cur_min)
            cur_min=min(cur_min,price)
        return max_profit
        