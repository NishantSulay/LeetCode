# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # LCA must be between p and q and exist within the subtree of the node being checked. 
        # Left subtree of a node N contains nodes whose values are lesser than or equal to node N's value
        # Right subtree of a node N contains nodes whose values are greater than node N's value
        # Both left and right subtree's are also BST 
        
        
        # Use recursion to check if p and q exist in Node N's subtrees.
        # Starting at the root node if both p and q are in the right subtree than traverse right subtree
        # if p and q are in the left subtree than traverse the left subtree
        # if both p and q not in left subtree or right subtree than that is the LCA. 
        
        LCA = root
        #right subtree
        if(q.val> LCA.val and p.val >LCA.val):
            return self.lowestCommonAncestor(LCA.right, p, q)
          
        #left
        elif(q.val < LCA.val and p.val <LCA.val):
            return self.lowestCommonAncestor(LCA.left, p, q)
        
        else: 
            return LCA

       
    
        
        