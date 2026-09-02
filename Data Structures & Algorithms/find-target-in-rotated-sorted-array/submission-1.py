class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)-1
        while left<=right:
            
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<nums[right]: #首先判断断点,这种情况断点在左边
                if target>nums[right]:
                    right=mid-1
                elif target==nums[right]:
                    return right
                elif target<nums[right]:
                    if target>nums[mid]:
                        left=mid+1
                    elif target<nums[mid]:
                        right=mid-1

            elif nums[mid]>nums[right]:#首先判断断点,这种情况断点在右边
                if target<nums[left]:
                    left=mid+1
                elif target==nums[left]:
                    return left
                elif target>nums[left]:
                    if target>nums[mid]:
                        left=mid+1
                    elif target<nums[mid]:
                        right=mid-1
            else:
                return -1
        return -1

 
            