# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        queue1=deque([p])
        queue2=deque([q])
        while queue1 or queue2:
            element1=queue1.popleft()
            element2=queue2.popleft()
            if not element1 or not element2:
                return False
            if element1.val!=element2.val:
                return False
            if element1.left and not element2.left:
                return False
            elif not element1.left and element2.left:
                return False
            elif element1.left and element2.left:
                queue1.append(element1.left)
                queue2.append(element2.left)
            else:
                pass
            if element1.right and not element2.right:
                return False
            elif not element1.right and element2.right:
                return False
            elif element1.right and element2.right:
                queue1.append(element1.right)
                queue2.append(element2.right)
        return True