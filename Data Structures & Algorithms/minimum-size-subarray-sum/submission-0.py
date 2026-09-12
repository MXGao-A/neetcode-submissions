class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length=float("inf")
        left=0
        cur_sum=0
        for right, num in enumerate(nums):
            cur_sum+=num
            while cur_sum>=target:
                min_length=min(min_length,right-left+1)
                cur_sum-=nums[left]
                left+=1
        return min_length if min_length!=float("inf") else 0
                