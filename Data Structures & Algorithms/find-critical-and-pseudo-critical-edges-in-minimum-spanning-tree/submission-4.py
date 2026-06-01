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
        sorted_edges = sorted(enumerate(edges), key=lambda x: x[1][2])
        sorted_edges = [(w,u,v,idx) for idx,(u,v,w) in sorted_edges]

        def kruk(exculded=None,forced_edge = None):
            egdes_used_in_mst = set()
            union_set = UnionSet(n)
            mst_weight = 0 
            if forced_edge:
                union_set.union(forced_edge[1],forced_edge[2])
                mst_weight += forced_edge[0]
                egdes_used_in_mst.add(forced_edge[3])

            idx= 0 
            while idx < len(sorted_edges):
                w,u,v,j = sorted_edges[idx]
                parent_u = union_set.find(u)
                parent_v = union_set.find(v)
                if  parent_u == parent_v   or (w,u,v) == exculded or (w,v,u) == exculded:
                    idx+= 1 
                    continue
                egdes_used_in_mst.add(j)
                union_set.union(u,v)
                mst_weight += w 
                idx += 1 
                
            
            return mst_weight,union_set.is_connected(),egdes_used_in_mst



        
        crit = []
        pseudo = []
        egdes_used_in_mst = set()
        mst_weight,_,egdes_used_in_mst= kruk()

        for idx,(u,v,w) in enumerate(edges):
            new_weight,is_connected,_ = kruk(exculded=(w,u,v))

            if new_weight > mst_weight or not is_connected:
                crit.append(idx)
            else:
                pseudo.append(idx)

        for idx,(u,v,w) in enumerate(edges):
            new_weight,is_connected,edg_set = kruk(forced_edge=(w,u,v,idx))
            if is_connected and new_weight == mst_weight:
                egdes_used_in_mst = egdes_used_in_mst.union(edg_set)


        idx= 0 
        for idx,edge in enumerate(pseudo):
            if edge not in egdes_used_in_mst:
                pseudo[idx] = None
        
        new_pseduo = []
        for edg in pseudo:
            if edg != None :
                new_pseduo.append(edg)
        
            
       
        return [crit,new_pseduo]
