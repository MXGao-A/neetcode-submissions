class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj_list=[[] for i in range(numCourses)]
        for pre in prerequisites:
            adj_list[pre[1]].append(pre[0])
        state=[0]*numCourses
        def dfs(node):
            if state[node]==1:
                return False
            if state[node]==2:
                return True
            state[node]=1
            for neighbor in adj_list[node]:
                if not dfs(neighbor):
                    return False
            state[node]=2
            return True
        for s in range(numCourses):
            if not dfs(s):
                return False
        return True
