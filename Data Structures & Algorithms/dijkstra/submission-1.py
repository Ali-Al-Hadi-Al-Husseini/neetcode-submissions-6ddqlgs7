class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj_list = [[] for _ in range(n)]
        paths = {i:-1 for i in range(n)}

        for u,v,w in edges:
            adj_list[u].append((w,v))


        min_heap = [(0,src)]
        
        while min_heap:
            curr_weight,curr_node = heapq.heappop(min_heap)

            if curr_weight < paths[curr_node] or paths[curr_node] == -1 :
                paths[curr_node] = curr_weight

            for weight,node in adj_list[curr_node]:
                if weight +curr_weight < paths[node] or  paths[node] == -1:
                    heapq.heappush(min_heap,(weight+curr_weight, node))
                    paths[node] =weight +curr_weight  

        return paths
        