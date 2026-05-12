class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # kruskal's algo
        n = len(points)
        parents = [-1 for _ in range(n)]
        distance_heap = []

        for i in range(n):
            for j in range(i +1,n):
                x1,y1 = points[i]
                x2,y2 = points[j]
                manhattan = abs(x1 -x2) + abs(y1-y2)
                heapq.heappush(distance_heap,(manhattan,(i,j)))

        total = 0   
        while distance_heap:
            curr_cost,(v, u) = heapq.heappop(distance_heap)
            parent_v = get_parent(v,parents)
            parent_u = get_parent(u,parents)
            if parent_u == parent_v :
                continue

            if parents[parent_v] <= parents[parent_u]:
                parents[parent_v] += parents[parent_u]
                parents[parent_u] = parent_v
            else:
                parents[parent_u] += parents[parent_v]
                parents[parent_v] = parent_u

            total += curr_cost


            
        return total
            

        
def get_parent(ver,parents):
    parent = ver
    while parents[parent] >= 0:
        parent = parents[parent]
    return parent
        