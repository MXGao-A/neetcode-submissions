# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        max_res=0
        slow,fast=head,head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        #now slow is at the start of the second half, now time to reverse the second half
        # 1,2,3,4,5,6

        cur=slow
        prev=None
        while cur:
            next_node=cur.next
            cur.next=prev
            prev=cur
            cur=next_node
        left=head
        right=prev
        while right:
            max_res=max(left.val+right.val,max_res)
            left=left.next
            right=right.next

        return max_res
            
