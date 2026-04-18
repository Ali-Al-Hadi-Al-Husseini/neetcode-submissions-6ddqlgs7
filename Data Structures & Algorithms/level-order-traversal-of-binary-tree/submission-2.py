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
    stack = []
    stack.append((root,0))

    while stack:
        curr,level = stack.pop()
        if curr == None : continue 
        if level not in order:
            order[level] = []
        
        order[level].append(curr.val)

        if curr.right != None :
            stack.append((curr.right,level + 1))
        if curr.left != None :
            stack.append((curr.left, level + 1))

