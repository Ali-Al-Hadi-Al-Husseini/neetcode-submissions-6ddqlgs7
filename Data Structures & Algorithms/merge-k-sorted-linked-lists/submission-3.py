# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        dummy = ListNode()
        curr_node = dummy
        active_nodes = len(lists)
        already_removed = set()
        
        while active_nodes > 0:
            
            curr_min = ListNode(float("+inf")),0

            for idx, node in enumerate(lists):
                if  node is None:
                    if idx not in already_removed:
                        active_nodes -= 1
                        already_removed.add(idx)
                    continue
                curr_min = min(curr_min,(node,idx),key= lambda x: x[0].val )

            if curr_min[0].val == float("+inf"):
                break
            curr_node.next = curr_min[0]
            curr_node = curr_min[0]
            lists[curr_min[1]] = lists[curr_min[1]].next

            # print([node.val if node else node for node in lists])



        return dummy.next