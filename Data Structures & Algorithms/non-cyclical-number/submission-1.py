class Solution:
    def isHappy(self, n: int) -> bool:
        cur=str(n)
        appeared=set()
        while cur!="1":
            cur_sum=0
            for n in cur:
                n=int(n)
                cur_sum+=n*n
            cur=str(cur_sum)
            if cur in appeared:
                return False
            appeared.add(cur)
        return True
