# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        
        def dfsLeft(root, res):
            if not root:
                return 
            
            if root.left: 
                res.append(root.val)
                dfsLeft(root.left, res)
                
            if not root.left and root.right:
                res.append(root.val)
                dfsLeft(root.right, res)
                
            if not root.left and not root.right:
                return
                
        def dfsRight(root, res): 
            
                if root.right:
                    dfsRight(root.right, res)

                if not root.right and root.left:
                    dfsRight(root.left, res)
            
                if not root.right and not root.left:
                    return
                
                res.append(root.val)

    
        def dfsLeafs(root, res):
            if not root:
                return 
            
            if not root.right and not root.left: 
                res.append(root.val)    


                
            dfsLeafs(root.left,res)
            dfsLeafs(root.right,res)
            
            
        if root:
            res.append(root.val)
            
            if root.left:
                dfsLeft(root.left, res)
            
            if root.right or root.left: 
                dfsLeafs(root, res)
            
            if root.right:
                dfsRight(root.right, res)
            
            
       
            
        return res
    
            
        
        
        