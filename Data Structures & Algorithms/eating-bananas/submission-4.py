class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        search_length=max(piles)
        left,right=1,search_length
        cand=-1
        while left<=right:
            mid=(left+right)//2
            num_h=0
            rate=mid
            for pile in piles:
                num_h+=pile//rate if pile%rate==0 else pile//rate+1
            if num_h>h:
                left=mid+1
            elif num_h<h:
                right=mid-1
                cand=mid
            else:
                right=mid-1
                cand=mid
        
        return cand

