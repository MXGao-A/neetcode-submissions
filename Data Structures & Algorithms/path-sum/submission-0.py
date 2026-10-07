# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node,cur,targetSum):
            if not node:
                return False
            
            cur+=node.val
            if not node.left and not node.right and cur==targetSum:
                return True
            if dfs(node.left,cur,targetSum):
                return True
            if dfs(node.right,cur,targetSum):
                return True
            cur-=node.val
            return False
        return dfs(root,0,targetSum)
        