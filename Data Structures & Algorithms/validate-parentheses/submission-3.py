class Solution:
    def isValid(self, s: str) -> bool:
        left_p=set(["(","[","{"])
        right_p={")":"(","]":"[","}":"{"}
        stack=[]
        for st in s:
            if st in left_p:
                stack.append(st)
            elif st in right_p.keys():
                if len(stack)==0:
                    return False
                left=stack.pop()
                if left!=right_p[st]:
                    return False
        return False if stack else True
