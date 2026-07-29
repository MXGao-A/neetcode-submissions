class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans=0
        cur=0
        for i in range(len(nums)):
            if not cur and nums[i]==1:
                cur=1
            elif cur and nums[i]==0:
                ans=max(ans,cur)
                cur=0
            elif cur and nums[i]==1:
                cur+=1
        ans=max(cur,ans)
        return ans