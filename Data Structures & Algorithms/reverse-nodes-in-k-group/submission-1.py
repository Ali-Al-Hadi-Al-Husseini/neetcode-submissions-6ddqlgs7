# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        heads = [head]
        remainig = None
        curr_node = head
        length = 1

        while curr_node:
            next_node = curr_node.next
            if length % k == 0 :
                heads.append(curr_node.next)
                curr_node.next= None
            curr_node= next_node
            length += 1
        if heads and ( heads[-1] == None or length % k != 1 ):
            remainig = heads.pop()
        if not heads:
            return head

        reversed_heads = [ll_reverse(node) for node in heads]

        for head in reversed_heads:
            curr_node = head
            while curr_node:
                print(curr_node.val)
                curr_node = curr_node.next

        
        next_head = reversed_heads[0]
        for idx in range(len(reversed_heads) - 1):
            print("idx =",idx)
            curr_node = reversed_heads[idx]
            next_head = reversed_heads[idx + 1]

            while curr_node.next:
                curr_node= curr_node.next
            print(curr_node.val,next_head.val)
            curr_node.next = next_head
        
        while next_head.next:
            next_head= next_head.next
        
        next_head.next = remainig

        return reversed_heads[0]


def ll_reverse(head):
    
    curr_node = head
    prev_node = None
    while curr_node:
        next_node = curr_node.next

        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node

    return prev_node
        
