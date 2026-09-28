class Solution:
    def numDecodings(self, s: str) -> int:
        # let dp[i] be the number of ways to decode substring up to ith position. length of s
        dp=[0]*len(s)
        if s[0]!="0":
            dp[0]=1
        if len(s)==1:
            return dp[0]
        if s[1]!="0":
            dp[1]+=dp[0]
        if 10 <= int(s[0:2]) <= 26:
            dp[1]+=1
        for i in range(2,len(s)):
            if s[i]!="0":
                dp[i]+=dp[i-1]
            if 10<=int(s[i-1:i+1])<=26:
                dp[i]+=dp[i-2]
        return dp[-1]