class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix=0
        ans=0
        hash_map={0:-1}
        for j,num in enumerate(nums):
            if num==0:
                prefix-=1
            if num==1:
                prefix+=1
            if prefix in hash_map:
                ans=max(ans, j-(hash_map[prefix]+1)+1)
            else:
                hash_map[prefix]=j
        return ans

        # prefix[j]=prefix[i-1]
        # hash_map[prefix]=i-1

