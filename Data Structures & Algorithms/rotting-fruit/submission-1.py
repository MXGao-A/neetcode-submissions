from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten=[]
        ans=0
        m,n=len(grid),len(grid[0])
        num_fresh=0
        visited=set()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    num_fresh+=1
                if grid[i][j]==2:
                    rotten.append((i,j))
        queue=deque(rotten)
        if num_fresh==0:
            return 0
        if len(rotten)==0:
            return -1
        while queue:
            cnt=0
            for i in range(len(queue)):
                rot=queue.popleft()
                visited.add(rot)
                for direction in [[1,0],[-1,0],[0,1],[0,-1]]:
                    new_i,new_j=rot[0]+direction[0],rot[1]+direction[1]
                    if (new_i<0 or new_i>=m or new_j<0 or new_j>=n):
                        continue
                    new=grid[new_i][new_j]
                    if new==1:
                        queue.append((new_i,new_j))
                        grid[new_i][new_j]=2
                        num_fresh-=1
                        cnt+=1
            
            if cnt==0:
                break
            ans+=1
        if num_fresh==0:
            return ans
        else:
            return -1
        
                

        