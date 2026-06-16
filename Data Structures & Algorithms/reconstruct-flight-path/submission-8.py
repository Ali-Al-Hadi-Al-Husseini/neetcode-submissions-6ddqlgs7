from collections import defaultdict 
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list = defaultdict(list)
        for tick in tickets:
            adj_list[tick[0]].append(tick[1])
        
        for airport in adj_list:
            adj_list[airport].sort(reverse=True)

        path = []
        def dfs(source):
            nonlocal path

            while adj_list[source]:
                destination  = adj_list[source].pop()
                dfs(destination)
            path.append(source)

            return False 
        dfs("JFK")
        return path[::-1]




