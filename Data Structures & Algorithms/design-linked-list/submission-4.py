class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None
    

class MyLinkedList:
    def __init__(self):
        self.size=0
        self.head=None
        self.tail=None
        

    def get(self, index: int) -> int:
        if index>=self.size or index<0:
            return -1
        else:
            num_visited=1
            cur=self.head
            while num_visited<=index:
                cur=cur.next
                num_visited+=1
            return cur.val

    def addAtHead(self, val: int) -> None:
        if not self.size:
            new_node=ListNode(val)
            self.head=new_node
            self.tail=new_node
            self.size=1
        else:
            new_node=ListNode(val)
            self.head.prev=new_node
            new_node.next=self.head
            self.head=new_node
            self.size+=1

    def addAtTail(self, val: int) -> None:
        if not self.size:
            new_node=ListNode(val)
            self.head=new_node
            self.tail=new_node
            self.size=1
        else:
            new_node=ListNode(val)
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
            self.size+=1


    def addAtIndex(self, index: int, val: int) -> None:
        if index==self.size:
            self.addAtTail(val)
        elif index>=self.size:
            return 
        elif index==0:
            self.addAtHead(val)
        else:
            new_node=ListNode(val)
            num_visited=1
            cur=self.head
            while num_visited<=index:
                cur=cur.next
                num_visited+=1
            old_ith_node=cur
            old_prev=old_ith_node.prev
            old_prev.next=new_node
            new_node.prev=old_prev
            old_ith_node.prev=new_node
            new_node.next=old_ith_node
            self.size+=1

        

    def deleteAtIndex(self, index: int) -> None:
        if index>=self.size or (not self.size):
            return 
        else:
            num_visited=1
            cur=self.head
            while num_visited<=index:
                cur=cur.next
                num_visited+=1
            old_ith_node=cur
            old_prev=old_ith_node.prev
            old_next=old_ith_node.next
            if old_prev and old_next:
                old_prev.next=old_next
                old_next.prev=old_prev
            elif old_prev and (not old_next):
                old_prev.next=None
                self.tail=old_prev
            elif old_next and (not old_prev):
                old_next.prev=None
                self.head=old_next
            self.size-=1

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)