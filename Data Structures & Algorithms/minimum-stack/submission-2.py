class MinStack:

    def __init__(self):
        self.stack=[]
        self.size=0
        self.Min=[float("inf")]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.size+=1
        cur_min=min(self.Min[-1],val)
        self.Min.append(cur_min)


    def pop(self) -> None:
        self.stack.pop()
        self.size-=1
        self.Min.pop()
        

    def top(self) -> int:
        return self.stack[self.size-1]
        

    def getMin(self) -> int:
        return self.Min[-1]
