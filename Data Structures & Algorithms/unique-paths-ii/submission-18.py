class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp=[[0]*n for i in range(m)]
        if obstacleGrid[0][0]==1:
            return 0
        dp[0][0]=1
        blocking_cnt=n
        for j in range(1,n):
            if obstacleGrid[0][j]==1:
                dp[0][j]=0
                blocking_cnt=j
                break
            else:
                dp[0][j]=1
        for j in range(blocking_cnt+1,n):
            dp[0][j]=0
        for i in range(1,m):
            for j in range(n):
                if obstacleGrid[i][j]==1:
                    dp[i][j]=0
                    continue
                if j>=1:
                    dp[i][j]+=dp[i][j-1]
                
                dp[i][j]+=dp[i-1][j]
    
        return dp[-1][-1]
