class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp=[1]*len(nums)
        M=[-float("inf")]*len(nums)
        m=[float("inf")]*len(nums)
        res=-float('inf')
        for i in range(len(nums)):
            if i==0:
                M[i]=max([nums[i]])
                m[i]=min([nums[i]])
            else:
                M[i]=max([nums[i],nums[i]*M[i-1],nums[i]*m[i-1]])
                m[i]=min([nums[i],nums[i]*M[i-1],nums[i]*m[i-1]])
            res=max(res,M[i])
        return res