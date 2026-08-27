class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix=[0]*len(nums)
        for i,num in enumerate(nums):
            prefix[i]=num+prefix[i-1] if (i-1)>=0 else num
        
        postfix=[0]*len(nums)
        i=len(nums)-1
        for num in nums[::-1]:
            postfix[i]=num+postfix[i+1] if i+2<=len(nums) else num
            i-=1
        for i,num in enumerate(prefix):
            if prefix[i]==postfix[i]:
                return i
        return -1
        