# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        queue = collections.deque()
        level = 0 
        
        if root:
            queue.append(root)
            
        while queue:
            
            
            if level%2 != 0:
                l, r = 0, len(queue)-1
                
                while l<r:
                    queue[l].val, queue[r].val = queue[r].val, queue[l].val
                    l +=1
                    r -=1
                    
            for _ in range(len(queue)):
                
                node = queue.popleft()

                if node.right or node.left:
                    queue.append(node.left)
                    queue.append(node.right)

            level +=1
                    

                            
        return root
                        
                        
                
        