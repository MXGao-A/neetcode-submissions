from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q=deque()
        ans=[]
        if len(nums)==1 and k>=1:
            return [nums[0]]
        
        for right, num in enumerate(nums):
            while q and num>=nums[q[-1]]:
                q.pop()

            q.append(right)

            if q[0]<right-k+1:
                q.popleft()

            if right>=k-1:
                ans.append(nums[q[0]])
            
        return ans