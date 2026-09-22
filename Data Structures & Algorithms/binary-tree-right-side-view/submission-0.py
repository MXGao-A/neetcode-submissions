# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue=deque()
        queue.append(root)
        res=[]
        while queue:
            level_size=len(queue)
            for i in range(len(queue)):
                element=queue.popleft()
                if i==level_size-1:
                    res.append(element.val)
                if element.left:
                    queue.append(element.left)
                if element.right:
                    queue.append(element.right)
        return res