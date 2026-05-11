class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        probabilities = [0 for _ in range(n)]
        adj_list = [[] for _ in range(n)]

        for i in range(len(edges)):
            u,v = edges[i]
            p = succProb[i]
            adj_list[u].append((p,v))
            adj_list[v].append((p,u))
        

        min_heap= [(-1, start_node)]
        visited = set()

        while min_heap:
            curr_proba, curr_node = heapq.heappop(min_heap)
            if curr_node == end_node:
                return curr_proba * -1 
            visited.add(curr_node)
            for proba, node in adj_list[curr_node]:
                new_proba = curr_proba * proba
                if probabilities[node] >= new_proba and node not in visited:
                    probabilities[node] = new_proba
                    heapq.heappush(min_heap,(new_proba,node))

        return probabilities[end_node] * -1

