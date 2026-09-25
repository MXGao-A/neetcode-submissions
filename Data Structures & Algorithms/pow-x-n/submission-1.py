class Solution:
    def myPow(self, x: float, n: int) -> float:
        # res=1
        # for i in range(abs(n)):
        #     res*=x
        # return res if n>0 else 1/res
        if x==0:
            return 0
        if n==0:
            return 1
        if n<0:
            x=1/x
            n=-n
        
        result = 1.0
        while n > 0:
            if n % 2 == 1:      
                result *= x
                n-=1
            x *= x              
            n //= 2             
        return result