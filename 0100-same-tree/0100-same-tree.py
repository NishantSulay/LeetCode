# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            
            if p.val != q.val:
                return False

            left = self.isSameTree(p.left, q.left)
            right = self.isSameTree(p.right, q.right)

            return left and right
        
        if not p and q:
            return False
        if p and not q:
            return False
        if not p and not q:
            return True
        