# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode(0)
        current = head
        
        while l1 is not None or l2 is not None:
            v1 = 0
            v2 = 0
            
            if l1 is not None:
                v1 = l1.val   
                
            if l2 is not None:
                v2 = l2.val
                
            
            newNode = ListNode(v1 + v2 + carry)
            carry, newNode.val = newNode.val//10, newNode.val%10
            
            current.next = newNode
            current = current.next
            
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
 
                
        if carry > 0:
            newNode = ListNode(carry)
            current.next = newNode
            current = current.next
            

        return head.next