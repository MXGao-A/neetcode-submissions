class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left,right=0,len(heights)-1
        max_area=0
        while left<right:
            cur_area=(right-left)*min(heights[left],heights[right])
            if heights[left]<=heights[right]:
                left+=1
            else:
                right-=1
            max_area=max(cur_area,max_area)
        return max_area
        