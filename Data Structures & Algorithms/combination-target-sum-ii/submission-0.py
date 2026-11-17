class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        nums.sort()

        def dfs(cur_array,cur_sum,cur_index):
            if cur_sum==target:
                res.append(cur_array[:])
                return
            if cur_sum>target:
                return 
            for i,num in enumerate(nums):
                if i<cur_index:
                    continue
                if i>cur_index and nums[i]==nums[i-1]:
                    continue
                cur_sum+=num
                cur_array.append(num)
                dfs(cur_array,cur_sum,i+1)

                cur_array.pop()
                cur_sum-=num


        dfs([],0,0)
        return res

        