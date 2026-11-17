class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        visited=set()

        max_area=0

        def dfs(i,j):
            if (i<0 or i>=m or j<0 or j>=n or (i,j) in visited or grid[i][j]!=1):
                return 0
            
            area=1
            visited.add((i,j))
            area+=dfs(i+1,j)
            area+=dfs(i-1,j)
            area+=dfs(i,j+1)
            area+=dfs(i,j-1)
            return area
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    max_area=max(dfs(i,j),max_area)
        return max_area