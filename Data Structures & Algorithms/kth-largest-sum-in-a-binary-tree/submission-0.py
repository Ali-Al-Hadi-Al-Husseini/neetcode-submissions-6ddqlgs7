# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        sums = []

        queue = deque()
        queue.append((root,1))
        curr_sum = 0 
        level = 1 

        while queue:
            curr_node,curr_lvl = queue.popleft()
            if curr_lvl != level :
                sums.append(curr_sum)
                curr_sum = 0 
                level  += 1 

            curr_sum += curr_node.val
            if curr_node.left : queue.append((curr_node.left,curr_lvl + 1 ))
            if curr_node.right : queue.append((curr_node.right,curr_lvl + 1 ))

        sums.append(curr_sum)
        sums.sort()

        return sums[-k] if len(sums) >=k else -1 