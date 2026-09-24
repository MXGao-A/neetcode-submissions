# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue = deque([root])
        while queue:
            element = queue.popleft()
            element.left, element.right = element.right, element.left
            if element.left:
                queue.append(element.left)
            if element.right:
                queue.append(element.right)
        return root