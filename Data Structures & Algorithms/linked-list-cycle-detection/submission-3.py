# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None : return False 
        slow = head
        fast = head.next

        while fast:
            if slow.val == fast.val:
                return True
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
                




        return False