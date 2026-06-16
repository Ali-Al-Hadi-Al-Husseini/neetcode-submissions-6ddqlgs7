from collections import defaultdict 
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list = defaultdict(list)
        for tick in tickets:
            heapq.heappush(adj_list[tick[0]],tick[1])


        path = []
        def dfs(source):
            nonlocal path

            while adj_list[source]:
                destination  = heapq.heappop(adj_list[source])
                dfs(destination)
            path.append(source)

            return False 
        dfs("JFK")
        return path[::-1]




