class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)
        dic={}
        for i, num in enumerate(nums):
            dic[num]=i
        
        def dfs(cur,cur_index_list):
            if len(cur)==n:
                res.append(cur.copy())
            
            for num in nums:
                if dic[num] in cur_index_list:
                    continue
                cur.append(num)
                cur_index_list.append(dic[num])
                dfs(cur,cur_index_list)
                cur.pop()
                cur_index_list.pop()
        dfs([],[])
        return res
