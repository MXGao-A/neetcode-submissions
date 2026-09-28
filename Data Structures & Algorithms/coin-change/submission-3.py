class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float("inf")]*(amount+1)
        dp[0]=0
        for i in range(1,amount+1):
            val=float("inf")
            for c in coins:
                if i-c<0:
                    continue
                val=min(val,dp[i-c])
            dp[i]=val+1
        return dp[amount] if dp[amount]!=float("inf") else -1



