# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # queue=deque([(p,q)])
        # while queue:
        #     a,b=queue.popleft()
        #     if not a and not b:
        #         continue
        #     if not a or not b:
        #         return False
        #     if a.val!=b.val:
        #         return False
        #     queue.append((a.left,b.left))
        #     queue.append((a.right,b.right))
        # return True
        if not p and not q:
            return True
        elif not p or not q:
            return False
        if p.val!=q.val:
            return False
        left_same=self.isSameTree(p.left,q.left)
        right_same=self.isSameTree(p.right,q.right)
        return left_same and right_same
