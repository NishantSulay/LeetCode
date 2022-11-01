# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
      
        currNode = head 
        dummyNode = ListNode(0, head)
        leftPrev = dummyNode
        
        for i in range(left-1):
            leftPrev = currNode
            currNode = currNode.next
            
        
        prevNode = None
        
        
        for i in range(right-left+1):
            temp = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = temp
            
        
            
        leftPrev.next.next = currNode
        leftPrev.next = prevNode
        
        return dummyNode.next
        
        
        
        
            
        
            
            
            
            
            
        
            
            
        