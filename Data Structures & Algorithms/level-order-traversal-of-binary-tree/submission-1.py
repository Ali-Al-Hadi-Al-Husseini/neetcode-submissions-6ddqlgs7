class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        order = {}
        bfss(root, order)
        res= []
        idx = 0

        while idx in order:
            res.append(order[idx])
            idx += 1
        return res


def bfss(root, order):
    queue = []
    queue.append((root,0))

    while queue:
        curr,level = queue.pop(0)
        if curr == None : continue 
        if level not in order:
            order[level] = []
        
        order[level].append(curr.val)
        if curr.left != None :
            queue.append((curr.left, level + 1))

        if curr.right != None :
            queue.append((curr.right,level + 1))
