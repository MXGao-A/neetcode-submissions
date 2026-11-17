class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        nums.sort()
        
        def dfs(arr,cursum,index):
            if cursum==target:
                ans.append(arr.copy())
                return
            if cursum>target:
                return
            
            for i, num in enumerate(nums):
                if i<index:
                    continue
                if cursum+num>target:
                    break
                if i>index and nums[i-1]==nums[i]:
                    continue
                
                cursum+=num
                arr.append(num)
                dfs(arr,cursum,i+1)
                cursum-=num
                arr.pop()
        dfs([],0,0)
        return ans

        