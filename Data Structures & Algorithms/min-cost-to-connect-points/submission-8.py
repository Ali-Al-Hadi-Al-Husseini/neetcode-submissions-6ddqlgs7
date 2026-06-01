class UnionSet:
    def __init__(self,n: int):
        self.parents = [-1 for _ in range(n)]

    def find(self, ver: int) -> int:
        while self.parents[ver] >= 0:
            grandparent = self.parents[ver]
            if self.parents[grandparent] >= 0:
                self.parents[ver] = self.parents[grandparent]
            
            ver = self.parents[ver]
        return ver

    def union(self,ver1,ver2):
        parent_ver1 = self.find(ver1)
        parent_ver2 = self.find(ver2)

        if parent_ver1 == parent_ver2:
            return
        if  self.parents[parent_ver1] <= self.parents[parent_ver2]:
            self.parents[parent_ver1] += self.parents[parent_ver2]
            self.parents[parent_ver2] = parent_ver1
        else:
            self.parents[parent_ver2] += self.parents[parent_ver1]
            self.parents[parent_ver1] = parent_ver2




class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        union_set = UnionSet(n)

        min_heap = []
        mst_adj_list = [[] for _ in range(n)]
        adj_list = [[] for _ in range(n)]

        for i,(x1,y1) in enumerate(points):
            for j,(x2,y2 )in enumerate(points[i+1:n]):
                manhattan = abs(x1-x2) + abs(y1-y2)
                heapq.heappush(min_heap,(manhattan,i,j+i+1))

        while min_heap:
            w,u,v = heapq.heappop(min_heap)
            parent_u = union_set.find(u)
            parent_v = union_set.find(v)

            if  parent_u == parent_v and parent_u != -1  :
                continue
            mst_adj_list[u].append([v,w])
            mst_adj_list[v].append([u,w])

            union_set.union(u,v)


        def dfs(u,visited):
            curr_weight = 0

            for v,w in mst_adj_list[u]:
                if (u,v) in visited  or (v,u) in visited:
                    continue
                visited.add((u,v))
                curr_weight += dfs(v,visited) + w


            return curr_weight 

       
        return dfs(0,set())
