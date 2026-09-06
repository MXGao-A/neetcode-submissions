# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        #now snow is the mid point
        
        second=slow.next
        slow.next=None
        prev=None
        
        while second:
            next_node=second.next
            second.next=prev
            prev=second
            second=next_node

        
        #[0,1,2,3 None] [6,5,4,None]
        first=head
        second=prev
        while second:
            next_first=first.next
            next_second=second.next
            first.next=second
            second.next=next_first
            first=next_first
            second=next_second
        

            

