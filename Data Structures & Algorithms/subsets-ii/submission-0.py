class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()

        def dfs(arr,index):
            ans.append(arr.copy())

            for i, num in enumerate(nums):
                if i<index:
                    continue
                if i>index and nums[i]==nums[i-1]:
                    continue
                arr.append(num)
                dfs(arr, i+1)
                arr.pop()
        dfs([],0)
        return ans