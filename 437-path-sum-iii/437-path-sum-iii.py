# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        total_paths = 0 
        if not root:
            return 0
        
        def dfs(root, targetSum):
            nonlocal total_paths
            if root:        

                if targetSum == root.val:
                    total_paths += 1 
                    
                    
                dfs(root.left, targetSum - root.val)
                dfs(root.right, targetSum - root.val)
                
                    
                    
        dfs(root, targetSum)
        total_paths += self.pathSum(root.left, targetSum)
        total_paths += self.pathSum(root.right, targetSum)

        
        return total_paths