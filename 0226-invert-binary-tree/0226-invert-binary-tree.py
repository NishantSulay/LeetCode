# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        #bfs to invert levels , use collection.deque
        


        # iterative dfs, preorder traversal
        
        stack = []
        
        if root:
            stack.append(root)
        
        while len(stack) > 0:
            node = stack.pop()
            
            if node.left or node.right:
                node.left, node.right = node.right, node.left
                
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
                    
        return root
            
        
            
        