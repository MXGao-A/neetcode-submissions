# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast,slow=head.next,head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        second=slow.next
        slow.next=None
        prev=None
        while second:
            next_second=second.next
            second.next=prev
            prev=second
            second=next_second
        
        #[1,2,3,None] [1,2,None]
        #[1,2,None][1,2,None]
        first=head
        second=prev
        while second:
            
            if first.val==second.val:
                first=first.next
                second=second.next
            else:
                return False
        return True
