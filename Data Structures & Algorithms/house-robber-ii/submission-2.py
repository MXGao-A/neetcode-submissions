class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def subproblem(num_slice):
            if not num_slice:
                return 0
            if len(num_slice)==1:
                return num_slice[0]
            dp=[0]*len(num_slice)
            dp[0]=num_slice[0]
            dp[1]=max(num_slice[0],num_slice[1])
            for i in range(2,len(num_slice)):
                dp[i]=max(dp[i-2]+num_slice[i],dp[i-1])
            return dp[-1]
        return max(subproblem(nums[1:]),subproblem(nums[0:len(nums)-1]))
