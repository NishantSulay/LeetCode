# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        queue = deque()
        
        if not root:
            return res
        
        queue.append(root)
        
        while(len(queue) > 0):
            temp = []
            queue_len = len(queue)
            
            for i in range(queue_len):
                node = queue.popleft()
                temp.append(node.val)
                
                if node.left != None or node.right != None:
                    if node.left != None:
                        queue.append(node.left)
                    if node.right != None:
                        queue.append(node.right)
                

            res.append(temp)
            
        
        return res