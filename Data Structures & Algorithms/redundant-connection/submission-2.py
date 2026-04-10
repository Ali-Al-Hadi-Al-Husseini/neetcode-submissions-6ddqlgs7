class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parents = [-1 for _ in range(n + 1 )]

        result = []
        for edg in edges:
            ver1 = get_parent(edg[0],parents)
            ver2 = get_parent(edg[1],parents)
            if ver1 == ver2 :
                result = edg
            
            elif parents[ver1] >= parents[ver2]:
                parents[ver1] = ver2
                parents[ver2] -= 1
            else:
                parents[ver2] = ver1
                parents[ver1] -= 1 
        return result 


def get_parent(idx,parents):
    stack = []
    while parents[idx] >= 0:
        stack.append(idx)
        idx = parents[idx]
    
    for j in stack:
        parents[j] = idx      
    return idx