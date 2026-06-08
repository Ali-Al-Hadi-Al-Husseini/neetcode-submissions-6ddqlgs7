# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        curr_node = head
        prev_head = dummy
        curr_head = head
        length = 1

        while curr_node:
            if length % k != 0 :
                curr_node = curr_node.next
                length += 1
                continue
            next_node = curr_node.next
            rev_head = ll_reverse(curr_head,k)
            prev_head.next = rev_head

            prev_head = curr_head
            curr_head = next_node
            curr_node = next_node
            
            length += 1
        
        if curr_head:
            prev_head.next = curr_head


        return dummy.next
                    


def ll_reverse(head, k):
    
    curr_node = head
    prev_node = None
    while curr_node and k > 0:

        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node
        k -= 1
    # print("prev_node = ",prev_node.val)
    # tmp = prev_node 
    # while tmp:
    #     print(tmp.val)
    #     tmp =tmp.next
    return prev_node
        
