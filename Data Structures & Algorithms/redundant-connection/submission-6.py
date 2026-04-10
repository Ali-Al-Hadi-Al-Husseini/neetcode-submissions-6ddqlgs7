class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj_list = [[] for _ in range(len(edges) + 1 )]

        for edg in edges:
            adj_list[edg[0]].append(edg[1])
            adj_list[edg[1]].append(edg[0])

        visited = set()
        cycle,_,_ = dfs(1,adj_list,visited,1)


        idx = len(edges) -1 
        print(cycle)
        while idx > 0 :
            edg = edges[idx]
            if  tuple(edg) in cycle or tuple([edg[1],edg[0]]) in cycle:
                return edg
            idx -=1 

        return edges[0]

def dfs(idx,adj_list,visited,parent):
    if idx in visited:
        return {(parent,idx)}, idx, True

    visited.add(idx)
    cycle, start, pursue = None,None,None

    for neigh in adj_list[idx]:
        if neigh == parent:
            continue
        cycle, start, pursue = dfs(neigh, adj_list, visited,idx)
        if pursue:
            cycle.add((idx,neigh))
        if idx == start  :
            return cycle, start, False
        if pursue != None  :
            break 

    return cycle, start, pursue 

