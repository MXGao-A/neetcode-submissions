# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count=0
        cur=head
        while cur:
            count+=1
            cur=cur.next
        ind_from_st=count-n+1
        if count==1:
            return None
        if ind_from_st==1:
            return head.next
        cur=head
        x=1
        while cur:
            if x==ind_from_st-1:
                if cur.next:
                    next_node=cur.next.next
                    cur.next=next_node
                else:
                    next_node=None
                    cur.next=next_node
            
            x+=1
            cur=cur.next
        return head
