class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf") for _ in range(n)]
        adj_list = [[] for _ in range(n)]

        for _from,to,price in flights:
            adj_list[_from].append((price,to))

        prices[src]= 0
        flight_heap = [(0,-1,src)]
        visited = set()

        while flight_heap:
            curr_cost,curr_stops, curr_airport = heapq.heappop(flight_heap)
            if curr_airport == dst:
                return curr_cost
            if curr_airport in visited or curr_stops >=k:
                continue
            


            
            for cost,airport in adj_list[curr_airport]:
                new_cost = curr_cost + cost
                new_stops = curr_stops + 1
                if prices[airport] > new_cost:
                    heapq.heappush(flight_heap,(new_cost,new_stops,airport))


        return -1