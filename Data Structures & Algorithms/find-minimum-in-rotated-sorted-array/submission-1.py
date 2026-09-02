class Solution:
    def findMin(self, nums: List[int]) -> int:
        left,right=0,len(nums)-1
        while left<=right:
            mid=(left+right)//2
            
            if left==right:
                break
                
            if nums[mid]<nums[mid+1] and nums[mid]<nums[mid-1]:
                return nums[mid]
            elif nums[mid]<nums[right]:
                right=mid-1
            elif nums[mid]>nums[right]:
                left=mid+1
            
            
        return nums[mid]