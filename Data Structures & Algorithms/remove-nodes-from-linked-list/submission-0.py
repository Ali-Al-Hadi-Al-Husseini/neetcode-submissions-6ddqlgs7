# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        new_head = reverse_ll(head)
        curr_node = new_head
        curr_max = new_head.val
        dummy = ListNode(0,curr_node)
        prev_node = dummy

        while curr_node:
            curr_max = max(curr_max, curr_node.val)
            next_node = curr_node.next
            if curr_node.val < curr_max :
                prev_node.next = next_node 
            else:
                prev_node = curr_node
            
            curr_node = next_node


        return reverse_ll(dummy.next)




def reverse_ll(head : ListNode) -> ListNode:
    curr_node = head
    prev_node = None

    while curr_node.next:
        next_node = curr_node.next

        curr_node.next = prev_node 
        prev_node = curr_node
        curr_node = next_node

    curr_node.next = prev_node

    return curr_node







