class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        
        def dfs(arr,cursum,index):
            if cursum==target:
                ans.append(arr.copy())
                return
            if cursum>target:
                return
            
            for i, num in enumerate(nums):
                if i<index:
                    continue
                cursum+=num
                arr.append(num)
                dfs(arr,cursum,i)
                cursum-=num
                arr.pop()
        dfs([],0,0)
        return ans

        