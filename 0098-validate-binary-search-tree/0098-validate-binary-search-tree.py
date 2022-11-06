# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
            
            
        left_bound = float(-inf)
        right_bound = float(inf)
        
        def isValidSubTree(root, left_bound, right_bound):
            
            if not root:
                return True
            
            
            if isValidSubTree(root.left, left_bound, root.val) and isValidSubTree(root.right, root.val, right_bound) and left_bound< root.val <right_bound:
                return True
            else:
                return False
            
        left = isValidSubTree(root.left, left_bound, root.val)
        right = isValidSubTree(root.right, root.val, right_bound)
        
        if left and right:
            return True
        else:
            return False
        
    
            