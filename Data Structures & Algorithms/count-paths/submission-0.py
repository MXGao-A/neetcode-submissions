class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0]*n for i in range(m)]
        dp[0][0]=1
        for j in range(1,n):
            dp[0][j]=dp[0][j-1]
        
        for i in range(1,m):
            for j in range(n):
                if j>0:
                    dp[i][j]+=dp[i][j-1]
                dp[i][j]+=dp[i-1][j]
        return dp[-1][-1]