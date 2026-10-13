class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp=nums[0]
        res=dp
        start=end=0
        cur_start=0
        for i in range(1,len(nums)):
            if nums[i]>=dp+nums[i]:
                dp=nums[i]
                cur_start=i
            else:
                dp=dp+nums[i]
            if res>dp:
                pass
            else:
                start=cur_start
                end=i
                res=dp
            
        return res