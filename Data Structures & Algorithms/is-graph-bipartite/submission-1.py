class DSU:

    def __init__(self,size):
        self.parents = [-1] * size

    def find(self,node):
        if self.parents[node] <0 :
            return node
        self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    def union(self,u,v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv :
            return False

        if self.parents[pu] <= self.parents[pv]:
            self.parents[pv] = pu 
        if self.parents[pu] > self.parents[pv]:
            self.parents[pu] = pv 

        return True

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        dsu = DSU(len(graph))

        for node in range(len(graph)):
            for neigh in graph[node]:
                if dsu.find(neigh) == dsu.find(node):
                    return False

                dsu.union(graph[node][0],neigh)

        return True

