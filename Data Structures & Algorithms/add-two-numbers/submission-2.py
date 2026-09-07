# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1=l1
        cur2=l2
        sum_cur=ListNode()
        head=sum_cur
        move_to_next=0
        while l1 or l2:
            
            if l1 and l2:
                sum_val=l1.val+l2.val
            elif l1 and (not l2):
                sum_val=l1.val
            elif (not l1) and l2:
                sum_val=l2.val
            else:
                pass
            if move_to_next:
                sum_val+=1
                move_to_next=0
            else:
                pass
            move_to_next=sum_val//10
            cur_val=sum_val%10
            sum_cur.next=ListNode(cur_val)
            sum_cur=sum_cur.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        if move_to_next:
            sum_cur.next=ListNode(1)
        return head.next
            
             
