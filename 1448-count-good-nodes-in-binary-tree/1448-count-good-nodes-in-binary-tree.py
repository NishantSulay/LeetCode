# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        if root.left is None and root.right is None:
            return 1
        
        res = []
        
        def dfs(node, path):
            if node is None:
                return
            
            
            good = True
            for i in path:
                if i > node.val:
                    good = False

            if good:
                res.append(path + [node.val])
            
            dfs(node.left, path + [node.val])
            dfs(node.right, path + [node.val])
                    

                
        dfs(root, [])
            
        return len(res)
        