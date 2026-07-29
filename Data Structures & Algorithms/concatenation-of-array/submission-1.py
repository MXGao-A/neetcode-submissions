class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        size=len(nums)
        ans=[0]*(2*size)
        for i in range(len(ans)):
            ans[i]=nums[(i%size)]
        return ans