# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        arr = convert_to_list(root)
        
        return ";:;".join(arr)
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        parts = data.split(";:;")
        res = []
        if parts == ['']:
            return None

        for part in parts:
            if part[0] == "N":
                res.append(None)
                continue
            res.append(int(part))
        
        return convert_to_tree(res)
        


def convert_to_tree(arr):
    if not arr:
        return None

    root = TreeNode(arr[0])
    queue = deque([root])
    
    i = 1
    while i < len(arr):
        curr_node = queue.popleft()


        if i < len(arr):
            if arr[i] is not None:
                curr_node.left = TreeNode(arr[i])
                queue.append(curr_node.left)
            i += 1


        if i < len(arr):
            if arr[i] is not None:
                curr_node.right = TreeNode(arr[i])
                queue.append(curr_node.right)
            i += 1

    return root


def convert_to_list(node):
    if not node:
        return []
    queue =deque()
    queue.append(node)
    res = []
    
    while queue:
        curr_node = queue.popleft()
        if not curr_node:
            res.append("None")
            continue

        res.append(str(curr_node.val))
        queue.append(curr_node.left)
        queue.append(curr_node.right)

    while res[-1] == "None":
        res.pop()
    return res 

def get_indcies(idx):
    return (2 * idx) + (1) , (2 * idx) + (2)
