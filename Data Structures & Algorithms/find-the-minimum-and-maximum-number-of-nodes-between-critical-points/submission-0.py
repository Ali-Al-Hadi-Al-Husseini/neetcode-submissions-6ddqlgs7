# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        curr_node = head
        mid_node = head.next
        if not mid_node.next:
            return [-1,-1]

        next_node = mid_node.next

        max_dis = -1 
        min_dis = float("inf")
        curr = 2
        
        first_critcal = -1 # to track the max_dis
        last_critcal = -1  # to track min_dis
        
        while next_node :
            
            is_greater = mid_node.val > next_node.val  and mid_node.val > curr_node.val
            is_smaller = mid_node.val < next_node.val  and mid_node.val < curr_node.val
            is_critcal = is_greater or is_smaller

            if is_critcal: 
                if last_critcal != -1:
                    min_dis = min(min_dis, curr - last_critcal)
                if first_critcal == -1 :
                    first_critcal =curr
                else:
                    max_dis = max(max_dis, curr - first_critcal )

                last_critcal = curr
                
            curr_node = curr_node.next
            mid_node = mid_node.next
            next_node =next_node.next
            curr+= 1



        return [min_dis,max_dis] if max_dis != -1 and min_dis != float("inf") else [-1,-1]