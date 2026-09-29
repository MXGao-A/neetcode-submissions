class Solution:
    def numWays(self, n: int, k: int) -> int:
        dp=[[0]*2 for i in range(n)]
        dp[0][0]=k
        dp[0][1]=0
        for i in range(1,n):
            dp[i][0]=(k-1)*(dp[i-1][0]+dp[i-1][1])
            dp[i][1]=1*dp[i-1][0]
        return dp[n-1][0]+dp[n-1][1]