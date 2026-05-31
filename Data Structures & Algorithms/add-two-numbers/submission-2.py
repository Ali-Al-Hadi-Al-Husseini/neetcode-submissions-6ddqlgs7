# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr_node = dummy

        carry = 0

        while l1 or l2 or carry:
            curr_num = carry
            curr_num += l1.val if l1 else 0
            curr_num += l2.val if l2 else 0
            carry= 0
            
            if curr_num >= 10:
                new_curr = curr_num % 10 
                carry = (curr_num - new_curr) // 10
                curr_num = new_curr

            curr_node.next = ListNode(curr_num)
            curr_node = curr_node.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None 
            
        return dummy.next
