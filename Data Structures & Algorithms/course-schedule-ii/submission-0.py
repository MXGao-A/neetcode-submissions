class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans=[]
        graph=[[]for i in range(numCourses)]
        for a,b in prerequisites:
            graph[b].append(a)
        state=[0]*numCourses

        def dfs(node):
            if state[node]==2:
                return True
            if state[node]==1:
                return False
            state[node]=1
            for pre in graph[node]:
                if not dfs(pre):
                    return False
            state[node]=2
            ans.append(node)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return ans[::-1]