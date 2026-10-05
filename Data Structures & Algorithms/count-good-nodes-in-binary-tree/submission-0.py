# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        num_of_good=0
        def dfs(node,max_so_far):
            if node.val>=max_so_far:
                nonlocal num_of_good
                num_of_good+=1
            
            if node.left:
                dfs(node.left,max(max_so_far,node.val))
            if node.right:
                dfs(node.right,max(max_so_far,node.val))
        dfs(root,root.val)
        return num_of_good