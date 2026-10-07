class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)
        dic={}
        for i, num in enumerate(nums):
            dic[num]=i
        used=[False]*n
        def dfs(cur,cur_index_list):
            if len(cur)==n:
                res.append(cur.copy())
            
            for num in nums:
                if used[dic[num]]==True:
                    continue
                cur.append(num)
                cur_index_list.append(dic[num])
                used[dic[num]]=True
                dfs(cur,cur_index_list)
                cur.pop()
                cur_index_list.pop()
                used[dic[num]]=False
        dfs([],[])
        return res
