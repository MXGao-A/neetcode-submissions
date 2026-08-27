class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        premult=[1]*len(nums)
        for i,num in enumerate(nums):
            premult[i]=num*premult[i-1] if (i-1)>=0 else num
        
        postmult=[1]*len(nums)
        i=len(nums)-1
        for num in nums[::-1]:
            postmult[i]=num*postmult[i+1] if (i+1)<=(len(nums)-1) else num
            i-=1
        res=[1]*len(nums)
        for i, num in enumerate(nums):
            if (i+1)>len(nums)-1:
                res[i]=premult[i-1]
            elif (i-1)<0:
                res[i]=postmult[i+1]
            elif (i-1)>=0 and (i+1)<=len(nums)-1:
                res[i]=premult[i-1]*postmult[i+1]
        return res
