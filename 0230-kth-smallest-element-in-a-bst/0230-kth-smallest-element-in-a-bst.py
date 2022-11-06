# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        #in -order traversal
        # because BST, left child is < parent node and 
        # right child is greater than parent node
        # all nodes in right subtree larger than root
        # all nodes in left subtree smallre than root
        
        res = []
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
            
        dfs(root)
        
        return res[k-1]
        
        