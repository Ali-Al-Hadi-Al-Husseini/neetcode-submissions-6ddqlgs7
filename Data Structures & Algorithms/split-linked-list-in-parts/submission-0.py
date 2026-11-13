# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
            n = 0

            curr_node = head
            while curr_node:
                curr_node = curr_node.next
                n +=1 

            res = []
            part_size = n // k 
            remainder = n % k 
            curr_node = head

            for _ in range(k):
                res.append(curr_node)

                for _ in range(part_size-1):
                    if curr_node:
                        curr_node = curr_node.next

                if remainder > 0  and curr_node and n > k :
                    curr_node = curr_node.next
                    remainder -= 1 


                if curr_node:
                    tmp = curr_node.next
                    curr_node.next = None 
                    curr_node = tmp 


            return res 