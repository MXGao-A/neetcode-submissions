class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        appeared=set()
        left=0
        for right, num in enumerate(nums):
            
            if right>k:
                appeared.remove(nums[left])
                left+=1
            
            if num in appeared:
                return True
            appeared.add(num)
        return False
            