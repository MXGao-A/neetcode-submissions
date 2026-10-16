class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cur_sum=0
        max_dp=[0]*len(nums)
        min_dp=[0]*len(nums)
        max_dp[0] = min_dp[0] = nums[0]
        maxval=-float("inf")
        minval=float("inf")
        array_sum=0
        for i,num in enumerate(nums):
            array_sum+=num
            if i!=0:
                max_dp[i]=max(max_dp[i-1]+num,num)
                min_dp[i]=min(min_dp[i-1]+num,num)

            maxval=max(maxval,max_dp[i])
            minval=min(minval,min_dp[i])
        if maxval<0:
            return maxval
        return max(maxval,array_sum-minval)


