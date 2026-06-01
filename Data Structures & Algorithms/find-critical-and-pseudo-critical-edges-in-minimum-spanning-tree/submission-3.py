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

    def is_connected(self):
        num_of_parents = 0

        for par in self.parents:
            if par < 0 :
                num_of_parents += 1
        # print(self.parents)
        return num_of_parents == 1 



class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        min_heap = []


        for idx,(u,v,w) in enumerate(edges):
            heapq.heappush(min_heap,[w,u,v,idx])
        
        def kruk(min_heap,exculded=None,forced_edge = None):
            egdes_used_in_mst = set()
            union_set = UnionSet(n)
            mst_weight = 0 
            if forced_edge:
                union_set.union(forced_edge[1],forced_edge[2])
                mst_weight += forced_edge[0]
                egdes_used_in_mst.add(forced_edge[3])

            while min_heap:
                w,u,v,idx = heapq.heappop(min_heap)
                parent_u = union_set.find(u)
                parent_v = union_set.find(v)
                if  parent_u == parent_v   or (w,u,v) == exculded or (w,v,u) == exculded:
                    continue
                egdes_used_in_mst.add(idx)
                union_set.union(u,v)
                mst_weight += w 
                
            
            return mst_weight,union_set.is_connected(),egdes_used_in_mst



        
        crit = []
        pseudo = []
        egdes_used_in_mst = set()
        mst_weight,_,egdes_used_in_mst= kruk(min_heap[:])
        # print(mst_weight)
        for idx,(u,v,w) in enumerate(edges):
            new_weight,is_connected,_ = kruk(min_heap[:],(w,u,v))
            # if idx == 5 :
                # print(new_weight,is_connected)
            if new_weight > mst_weight or not is_connected:
                crit.append(idx)
            else:
                pseudo.append(idx)

        for idx,(u,v,w) in enumerate(edges):
            new_weight,is_connected,edg_set = kruk(min_heap[:],forced_edge=(w,u,v,idx))

            if is_connected and new_weight == mst_weight:
                egdes_used_in_mst = egdes_used_in_mst.union(edg_set)
        print(egdes_used_in_mst)
        print(pseudo)
        idx= 0 
        for idx,edge in enumerate(pseudo):
            if edge not in egdes_used_in_mst:
                pseudo[idx] = None
        
        new_pseduo = []
        for edg in pseudo:
            if edg != None :
                new_pseduo.append(edg)
        
            
       
        return [crit,new_pseduo]
