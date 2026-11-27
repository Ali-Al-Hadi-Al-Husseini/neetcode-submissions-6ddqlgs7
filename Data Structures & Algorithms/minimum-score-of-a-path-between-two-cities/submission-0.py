class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n+1)]

        for a,b, dist in roads:
            adj_list[a].append((b,dist))
            adj_list[b].append((a,dist))


        result = float("inf")
        queue = deque()
        queue.append(1)
        visited = [False] * (n+1) 

        while queue:
            curr_node = queue.popleft()
            if visited[curr_node]:
                continue
            visited[curr_node] = True

            for neigh, dist in adj_list[curr_node]:
                result = min(result,dist)
                queue.append(neigh)



        return result
