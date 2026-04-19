# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next == None : return 
        # o(n) time and O(1) space
        
        slow_ptr,fast_ptr = head, head
        prev = None
        while fast_ptr and fast_ptr.next:
            prev = slow_ptr
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        if prev:
            prev.next = None 
        curr_node = slow_ptr
        prev = None

        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev
            prev = curr_node
            curr_node = next_node

        curr1 = head
        curr2 = prev 
        head = ListNode()

        while curr1 and curr2 :
            next1 = curr1.next
            next2 = curr2.next

            head.next = curr1
            curr1.next = curr2
            head = curr2

            curr1 = next1
            curr2 = next2

