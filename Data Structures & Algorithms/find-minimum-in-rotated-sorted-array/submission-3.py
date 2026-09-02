class Solution:
    def findMin(self, nums: List[int]) -> int:
        left,right=0,len(nums)-1
        while left<=right:
            mid=(left+right)//2
            
            if left==right:
                break
                
            elif nums[mid]<nums[right]:
                right=mid
            elif nums[mid]>nums[right]:
                left=mid+1
            
            
        return nums[mid]