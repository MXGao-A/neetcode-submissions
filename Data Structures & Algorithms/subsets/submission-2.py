class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans=[]

        def dfs(arr,index):
            ans.append(arr.copy())

            for i,num in enumerate(nums):
                if i<index:
                    continue
                arr.append(num)
                dfs(arr,i+1)
                arr.pop()
        dfs([],0)
        return ans