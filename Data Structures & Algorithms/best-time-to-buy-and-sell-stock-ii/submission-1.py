class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        for i, price in enumerate(prices):
            if i==0:
                continue
            res+=max(prices[i]-prices[i-1],0)
        return res