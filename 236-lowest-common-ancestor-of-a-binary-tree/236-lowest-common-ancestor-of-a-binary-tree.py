# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(root, p, q):
            if root:
                
                #update the lca to this node if node p and q exists in this subtree
                if root.val == p.val or root.val == q.val:
                    return root
                
                left = dfs(root.left, p, q) 
                right = dfs(root.right, p, q)
                #if it exists in the right tree and left tree then root is the common element
                if left and right:
                    return root
                if left:
                    return left
                if right:
                    return right

            else:
                return None

        return dfs(root ,p,q) 