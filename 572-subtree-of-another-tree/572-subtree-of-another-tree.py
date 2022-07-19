# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSame(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            
            if root == None or  subRoot == None:
                return (root == None and subRoot == None)
            
            elif root.val == subRoot.val:
                return isSame(root.left, subRoot.left) and isSame(root.right, subRoot.right)
            else: 
                return False
            
        
        if not subRoot:
            return False
        if not root:
            return False
        
        elif isSame(root, subRoot):
            return True
        else: 
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        

        

            
            