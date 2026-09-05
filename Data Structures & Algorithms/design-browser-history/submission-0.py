class ListNode:
    def __init__(self,val):
        self.value=val
        self.prev=None
        self.next=None

class BrowserHistory:

    def __init__(self, homepage: str):
        new_node=ListNode(homepage)
        self.head=new_node
        self.tail=new_node
        self.cur_visit=self.head

    def visit(self, url: str) -> None:
        new_node=ListNode(url)
        self.cur_visit.next=new_node
        new_node.prev=self.cur_visit
        self.cur_visit=new_node
        
        

    def back(self, steps: int) -> str:
        count=1
        while count<=steps and self.cur_visit.prev:
            self.cur_visit=self.cur_visit.prev
            count+=1
        return self.cur_visit.value

    def forward(self, steps: int) -> str:
        count=1
        while count<=steps and self.cur_visit.next:
            self.cur_visit=self.cur_visit.next
            count+=1
        return self.cur_visit.value


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)