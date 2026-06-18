# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from math import gcd
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
            curr_node = head

            while curr_node.next:
                next_node = curr_node.next
                new_node = ListNode(gcd(curr_node.val,next_node.val))
                curr_node.next = new_node
                new_node.next = next_node
                curr_node = next_node



            return head 