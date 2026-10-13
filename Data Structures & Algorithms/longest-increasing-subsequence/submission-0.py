class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # res=0
        # for i in range(len(nums)-1):
        #     last=nums[i]
        #     size=1
        #     for j in range(i+1,len(nums)):
        #         if nums[j]<=last:
        #             continue
        #         else:
        #             size+=1
        #             last=nums[j]
        #     res=max(res,size)
        # return res

        dp=[0]*len(nums)
        dp[0]=1
        for i in range(1,len(nums)):
            cur_max=1
            for j in range(i):
                if nums[i]>nums[j]:
                    cur_max=max(cur_max,dp[j]+1)
            dp[i]=cur_max
        return max(dp)


