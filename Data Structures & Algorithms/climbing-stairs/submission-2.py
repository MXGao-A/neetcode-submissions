class Solution:
    def climbStairs(self, n: int) -> int:
        hash_map={}
        def f(n):
            if n==1:
                hash_map[n]=1
                return 1
            if n==2:
                hash_map[n]=2
                return 2
            if n in hash_map:
                return hash_map[n]
            else:
                hash_map[n]=f(n-1)+f(n-2)
                return f(n-1)+f(n-2)
        return f(n)