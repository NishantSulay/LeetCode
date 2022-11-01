# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        stack = [] 
        
        if root:
            stack.append((1,root))
            
        depth = 0
        while len(stack) > 0:
            curr_depth, root = stack.pop()
            
            if root:
                depth = max(curr_depth, depth)
                if root.left:
                    stack.append((curr_depth + 1, root.left))
                if root.right:
                    stack.append((curr_depth + 1, root.right))
                    
        
        return depth