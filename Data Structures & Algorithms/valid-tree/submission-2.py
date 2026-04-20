class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parents = [-1 for _ in range(n)]


        for edg in edges:
            ver1p = get_parent(edg[0], parents)
            ver2p = get_parent(edg[1], parents)

            if ver2p == ver1p:
                return False

            if parents[ver1p] <= parents[ver2p]:
                parents[edg[1]] = ver1p
                parents[ver1p] -= 1
            else:
                parents[edg[0]] = ver2p
                parents[ver2p] -= 1
        par_count = 0
        for par in parents:
            if par < 0 :
                par_count += 1 
        return par_count == 1



def get_parent(ver, parents):

    while parents[ver] >= 0:
        ver = parents[ver]
    return ver 