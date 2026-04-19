# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # o(n) time and O(n) space
        list_helper = []

        curr = head

        while curr:
            list_helper.append(curr)
            curr= curr.next

        new_list = [head]

        for i in range(1,len(list_helper)//2 +1  ):
            new_list.append(list_helper[-i])
            new_list.append(list_helper[i])

        if len(list_helper) % 2 == 0:
            new_list.pop()
        new_list.append(None)
        for idx in range(len(new_list) - 1):
            new_list[idx].next = new_list[idx + 1]

