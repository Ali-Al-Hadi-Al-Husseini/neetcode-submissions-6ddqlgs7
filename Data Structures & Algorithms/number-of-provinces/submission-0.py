class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        disjoint_set = DisJointSet(len(isConnected))

        for r in range(len(isConnected)):
            for c in range(len(isConnected)):
                if not isConnected[r][c]:
                    continue
                disjoint_set.union(r,c)
 


        provinces = 0
        for node in disjoint_set.parents:
            if node < 0 :
                provinces+=1

        return provinces


class DisJointSet:
    def __init__(self,size ):
        self.parents = [-1 for _ in range(size)]

    def union(self,u,v):
        p1,p2 = self.get_parent(u),self.get_parent(v)

        if p1== p2 and p1 >= 0 :
            return 
        if p1 <= p2 :
            self.parents[p1] += self.parents[p2]
            self.parents[p2] = p1
        else:
            self.parents[p2] += self.parents[p1]
            self.parents[p1] = p2


    def get_parent(self,city):
        curr = city
        limit = 10
        while self.parents[curr] >= 0 and limit :
            curr = self.parents[curr]
            limit -=1 
        
        return curr 




