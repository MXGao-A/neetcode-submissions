from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        queue = deque()
        INF=2147483647

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i, j))
        dist=1
        while queue:
            for i in range(len(queue)):
                x,y=queue.popleft()
                for dx,dy in [(1,0),[-1,0],[0,1],[0,-1]]:
                    nx,ny=x+dx,y+dy
                    if not (0<=nx<m) or not (0<=ny<n):
                        continue
                    if grid[nx][ny]==INF:
                        grid[nx][ny]=dist
                        queue.append((nx,ny))
            dist+=1
