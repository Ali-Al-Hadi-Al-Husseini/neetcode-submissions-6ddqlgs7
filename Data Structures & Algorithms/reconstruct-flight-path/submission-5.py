from collections import defaultdict 
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list = defaultdict(list)
        airports = set()
        for tick in tickets:
            heapq.heappush(adj_list[tick[0]],tick[1])
            airports.add(tick[0])
            airports.add(tick[1])

        path = []
        curr_path = []
        used_tickets = set()
        print(adj_list)
        def dfs(source):
            nonlocal curr_path,path
            curr_path.append(source)

            for _ in adj_list[source]:
                destiny = heapq.heappop(adj_list[source])
                if not dfs(destiny):
                    adj_list[source].append(destiny)
 
            if len(curr_path)== len(tickets)+1:
                path = curr_path[:]
                return True

            curr_path.pop()
            return False 
        dfs("JFK")
        return path




