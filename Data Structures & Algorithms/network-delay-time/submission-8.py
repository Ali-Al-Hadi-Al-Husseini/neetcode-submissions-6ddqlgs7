class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)


        for ui,vi,ti in times:
            adj_list[ui].append((ti,vi))

        time_needed = [float("inf")] * n
        time_needed[k -1] = 0
        min_heap = [(0,k)]
        visited = set()

        while min_heap:
            curr_time, curr_node = heapq.heappop(min_heap)
            if curr_node in visited:
                continue 
            visited.add(curr_node)

            for time,node in adj_list[curr_node]:
                new_time = curr_time + time 
                    
                if time_needed[node - 1] >= new_time:
                    time_needed[node - 1] = new_time
                    heapq.heappush(min_heap,(new_time,node))

        max_time = max(time_needed)
        return max_time if max_time < float("inf") else -1
