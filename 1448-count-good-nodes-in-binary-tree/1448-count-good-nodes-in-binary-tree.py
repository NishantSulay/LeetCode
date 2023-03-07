# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        if root.left is None and root.right is None:
            return 1
        
        res = 0
        
        def dfs(node, max_curr):
            nonlocal res
            
            if node is None:
                return
            
            if node.val >= max_curr:
                res += 1
                
            dfs(node.left, max(node.val, max_curr))
            dfs(node.right, max(node.val, max_curr))

        max_curr = root.val        
        dfs(root, max_curr)
            
        return res
        