# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        total =  str(get_sum(l1) + get_sum(l2))

        idx = len(total)-1
        dummy = ListNode()
        curr_node = dummy

        for num in reversed(total):
            curr_node.next= ListNode(int(num))
            curr_node = curr_node.next
        
        return dummy.next


    


def get_sum(ll):
    curr_sum = 0
    place = 1 

    while ll :
        curr_sum += ll.val * place
        place *= 10
        ll=ll.next
    print(curr_sum)
    return curr_sum