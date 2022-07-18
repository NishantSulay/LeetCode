# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        diameter = 0 
        if not root:
            return 0
        def longestPath(node):
            if not node:
                return 0
            nonlocal diameter
            left_path = longestPath(node.left)
            right_path = longestPath(node.right)
            diameter = max(diameter, left_path + right_path)
            
            return 1 + max(left_path, right_path)
        
        longestPath(root)
        return diameter
        