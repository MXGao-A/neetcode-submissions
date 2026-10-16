class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cur_sum=0
        max_dp=[0]*len(nums)
        min_dp=[0]*len(nums)
        maxval=-float("inf")
        minval=float("inf")
        array_sum=0
        for i,num in enumerate(nums):
            array_sum+=num
            max_dp[i]=max(max_dp[i-1]+num,num)
            min_dp[i]=min(min_dp[i-1]+num,num)

            maxval=max(maxval,max_dp[i])
            minval=min(minval,min_dp[i])
        if maxval<=0 and (array_sum-minval)<=0:
            return max(nums)
        return max(maxval,array_sum-minval)


