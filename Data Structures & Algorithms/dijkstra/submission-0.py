class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        paths = {i:float("inf") for i in range(n)}
        adj_list = [[] for _ in range(n)]
        for u,v,w in edges:
            adj_list[u].append((w,v))

        paths[src] = 0
        min_heap = [(0,src)]
        visited = set()
        while min_heap:
            curr_weight, curr_node = heapq.heappop(min_heap)
            if curr_node in visited :
                continue

            for weight,node in adj_list[curr_node]:
                if paths[node] >= curr_weight + weight:
                    heapq.heappush(min_heap,(curr_weight + weight,node))
                    paths[node] = min(paths[node],(curr_weight + weight))

        return {u:w if w != float("inf") else -1 for u,w in paths.items()}