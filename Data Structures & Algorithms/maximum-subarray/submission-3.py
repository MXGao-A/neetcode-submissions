class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp=nums[0]
        res=dp
        start=0
        end=None
        for i in range(1,len(nums)):
            if nums[i]>=dp+nums[i]:
                dp=nums[i]
                start_index=i
            else:
                dp=dp+nums[i]
            if res>dp:
                pass
            else:
                end=i
            res=max(res,dp)
        print(start,end)
        return res