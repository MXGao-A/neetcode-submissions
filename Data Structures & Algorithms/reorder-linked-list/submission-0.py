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
        mid=slow
        prev=None
        while slow:
            next_node=slow.next
            slow.next=prev
            prev=slow
            slow=next_node

        
        #[0,1,2,None] [3,2,None]
        #[0,1,2,3 None] [6,5,4,3,None]
        first=head
        second=prev
        while second!=mid:
            next_first=first.next
            next_second=second.next
            first.next=second
            second.next=next_first
            first=next_first
            second=next_second
        

            

