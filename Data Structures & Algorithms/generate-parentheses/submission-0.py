class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]

        def dfs(cur,left,right):
            if len(cur)==2*n and left==right:
                ans.append(cur)
                return 
            
            if left<n:
                dfs(cur+"(",left+1,right)
            
            if right<left:
                dfs(cur+")",left,right+1)
        dfs("",0,0)
        return ans