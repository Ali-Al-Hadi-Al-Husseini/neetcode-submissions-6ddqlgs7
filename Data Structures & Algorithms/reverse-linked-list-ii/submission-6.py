# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev_node = None
        curr_node = head
        position = 1

        while curr_node and position != left:
            prev_node = curr_node
            curr_node = curr_node.next
            position += 1

        
        left_node = curr_node
        before_left= prev_node
        
        
        while curr_node and position != (right + 1):
            temp = curr_node.next
            curr_node.next = prev_node 
            prev_node = curr_node
            curr_node = temp
            position += 1

        
        if left_node:
            left_node.next = curr_node
        if before_left:
            before_left.next = prev_node 

        return head if left_node is not  head else prev_node