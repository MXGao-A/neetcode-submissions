# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        last_cur=None
        while cur is not None:
            if cur==head:
                new_cur=cur.next
                cur.next=None
                last_cur=cur
                cur=new_cur
            else:
                new_cur=cur.next
                cur.next=last_cur
                last_cur=cur
                if new_cur is None:
                    head=cur
                    break
                else:
                    cur=new_cur
        return head
               
                    

