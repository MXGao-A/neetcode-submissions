class Solution:
    def calPoints(self, operations: List[str]) -> int:
        if not operations:
            return 0
        points_list=[]
        for operation in operations:
            if operation not in ["+","D","C"]:
                points_list.append(int(operation))
            elif operation == "+":
                points_list.append((points_list[-1]+points_list[-2]))
            elif operation == "D":
                points_list.append((points_list[-1]*2))
            elif operation == "C":
                points_list.pop()
        ans=0
        for point in points_list:
            ans+=point
        return ans