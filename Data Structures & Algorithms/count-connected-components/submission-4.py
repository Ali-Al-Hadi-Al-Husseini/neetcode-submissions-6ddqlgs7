class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [-1 for _ in range(n)]

        for edg in edges:
            v1p = get_parent(edg[0],parents)
            v2p = get_parent(edg[1],parents)
            if v1p == v2p:
                continue

            if parents[v1p] >= parents[v2p]:
                parents[v2p] = v1p
                parents[v1p] -= 1 
            else:
                parents[v1p] = v2p
                parents[v2p] -= 1 

        count = 0
        print(parents)
        for par in parents:
            if par < 0 :
                count += 1 
        return  count




def get_parent(idx,parents):

    while parents[idx] >= 0 :
        idx = parents[idx]

    return idx 