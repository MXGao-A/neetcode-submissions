# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        first=list1
        second=list2
        res=None
        if not first:
            return second
        elif not second:
            return first
        else: 
            dummy=ListNode()
            cur=dummy
            while first and second:
        
                if first.val<=second.val:
                    cur.next=first
                    cur=cur.next
                    first=first.next
                else:
                    cur.next=second
                    cur=cur.next
                    second=second.next
            if first:
                cur.next=first
            else:
                cur.next=second
            return dummy.next




            
