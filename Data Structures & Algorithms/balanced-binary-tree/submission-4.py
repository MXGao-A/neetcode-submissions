# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # if not root:
        #     return True
        
        # def height(node):
        #     if not node:
        #         return 0

        #     return 1+max(height(node.left),height(node.right))
        
        # if abs(height(root.left)-height(root.right))>1:
        #     return False


        # return self.isBalanced(root.left) and self.isBalanced(root.right)
        if not root:
            return True

        def height(node):
            if not node:
                return 0

            if abs(height(node.left)-height(node.right))>1:
                return -1
            
            if height(node.left)==-1 or height(node.right)==-1:
                return -1

            return 1+max(height(node.left),height(node.right))

        return height(root)!=-1