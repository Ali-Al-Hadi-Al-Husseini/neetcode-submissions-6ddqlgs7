class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        

        total = 0
        min_heap = [(0,points[0])]
        connected = set()

        while min_heap:
            curr_cost, (curr_x,curr_y) = heapq.heappop(min_heap)
            if (curr_x,curr_y)in connected:
                continue
            connected.add((curr_x,curr_y))
            total += curr_cost
            for x,y in points:
                if (x,y) in connected:
                    continue
                manhattan = abs(curr_x - x) + abs(curr_y - y)
                heapq.heappush(min_heap,(manhattan,(x,y)))
                
            


        return total