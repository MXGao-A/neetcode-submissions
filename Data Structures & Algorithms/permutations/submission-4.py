class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        n=len(nums)
        
        def dfs(arr,index_set):
            if len(arr)==n:
                ans.append(arr.copy())
                return 
            for i,num in enumerate(nums):
                if i in index_set:
                    continue
                arr.append(num)
                index_set.add(i)
                dfs(arr,index_set)
                index_set.remove(i)
                arr.pop()
               
        dfs([],set())
        return ans
