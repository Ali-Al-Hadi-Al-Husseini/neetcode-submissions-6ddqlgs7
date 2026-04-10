class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n)]

        for edg in edges:
            adj_list[edg[0]].append(edg[1])
            adj_list[edg[1]].append(edg[0])

        visited = set()
        component_count = 0
        for ver in range(n):
            if ver in visited:
                continue
            
            dfs(ver,adj_list,visited)
            component_count+=1 


        return component_count



def dfs(ver, adj_list, visited):
    if ver >= len(adj_list): return 
    visited.add(ver)
    
    for neigh in adj_list[ver]:
        if neigh in visited:continue
            
        dfs(neigh, adj_list, visited)
