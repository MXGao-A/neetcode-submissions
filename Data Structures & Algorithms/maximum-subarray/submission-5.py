class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        
        max_subarray=-float("inf")
        dp=[0]*len(nums)
        cur_sum=0
        for i,num in enumerate(nums):
            dp[i]=max(dp[i-1]+nums[i],nums[i])

            max_subarray=max(max_subarray,dp[i])
        return max_subarray
