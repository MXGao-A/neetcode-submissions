class Solution:
    def trap(self, height: List[int]) -> int:
        pre_max=[0]*len(height)
        ans=0
        for i,num in enumerate(height):
            if i>=1:
                pre_max[i]=max(pre_max[i-1],height[i])
            else:
                pre_max[i]=height[i]
        suf_max=[0]*len(height)
        i=len(height)-1
        while i>=0:
            if i<=len(height)-2:
                suf_max[i]=max(suf_max[i+1],height[i])
            else:
                suf_max[i]=height[i]
            i-=1
        for i,num in enumerate(height):
            if i!=0 and i!=len(height)-1:
                ans+=max(min(pre_max[i-1],suf_max[i+1])-height[i],0)
        return ans