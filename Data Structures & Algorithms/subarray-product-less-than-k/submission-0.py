class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        cur_prod=1
        left=0
        res=0
        for right in range(len(nums)):
            cur_prod*=nums[right]
            while left<=right and cur_prod>=k:
                cur_prod=cur_prod/nums[left]
                left+=1
            res+=right-left+1
        return res