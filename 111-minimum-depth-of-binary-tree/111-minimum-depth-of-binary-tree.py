# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        def dfs(root):
            
        
            if not root:
                return 0 
            
            if not root.left and not root.right:
                return 1
            
            elif not root.left and root.right:
                return 1+dfs(root.right)
            
            elif not root.right and root.left:
                return 1+dfs(root.left)
            
            else:
                return min(dfs(root.left), dfs(root.right)) + 1

        
        return dfs(root)