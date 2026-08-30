class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0]*len(temperatures)
        # for i,temperature in enumerate(temperatures):
        #     for j in range(i+1,len(temperatures)):
        #         if temperatures[j]>temperatures[i]:
        #             result[i]=j-i
        #             break
        #         else:
        #             pass
        # return result

        # the above one is a naive solution which takes O(n^2) time.
        # for example if encountering 30,27,28,29
        stack=[]
        for i,temperature in enumerate(temperatures):
            if not stack:
                stack.append((temperature,i))
            if temperature <= stack[-1][0]:
                stack.append((temperature,i))
            while stack and  temperature > stack[-1][0]:
                cur_element=stack.pop()
                result[cur_element[1]]=i-cur_element[1]
            stack.append((temperature,i))

        return result

