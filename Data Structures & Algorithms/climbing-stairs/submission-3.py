class Solution:
    def climbStairs(self, n: int) -> int:
        # hash_map={}
        # def f(n):
        #     if n==1:
        #         hash_map[n]=1
        #         return 1
        #     if n==2:
        #         hash_map[n]=2
        #         return 2
        #     if n in hash_map:
        #         return hash_map[n]
        #     else:
        #         hash_map[n]=f(n-1)+f(n-2)
        #         return f(n-1)+f(n-2)
        # return f(n)
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[-1]