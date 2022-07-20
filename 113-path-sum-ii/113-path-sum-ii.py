# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        if not root:
            return []
        
        output = []
        
        def currentPathSum(root: Optional[TreeNode], targetSum: int, currList: List[int]):
            nonlocal output
            
            if root:
                if not root.left and not root.right and targetSum == root.val : 
                    currList += [root.val]
                    output.append(currList)
                
                else:
                    
                    currentPathSum(root.left, targetSum - root.val, currList+[root.val])
                    currentPathSum(root.right,targetSum - root.val, currList+[root.val])

        currentPathSum(root, targetSum, [])            
        return output
    