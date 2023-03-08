# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        res = []
        
        def dfs(node):
            if node is None:
                return
            
            if node.left != None:
                dfs(node.left)
                
            res.append(node.val)
                
            if node.right != None:
                dfs(node.right)
        
        
        dfs(root)
        
        
        return res[k-1]