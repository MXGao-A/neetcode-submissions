class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for token in tokens:
            if token not in ['+',"-","*","/"]:
                stack.append(token)
            else:
                y=stack.pop()
                x=stack.pop()
                if token=="+":
                    result=int(x)+int(y)
                elif token=="-":
                    result=int(x)-int(y)
                elif token=="*":
                    result=int(x)*int(y)
                elif token=="/":
                    result=int(int(x)/int(y))
                stack.append(result)
        return int(stack[0])