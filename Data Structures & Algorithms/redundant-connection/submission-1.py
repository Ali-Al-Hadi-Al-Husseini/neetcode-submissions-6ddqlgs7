class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        all_ = set()
        for edg in edges :
            all_.add(edg[0])
            all_.add(edg[1])

        n = max(all_)
        del all_

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
    while parents[idx] >= 0:
        idx = parents[idx]
    return idx