class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj_list = defaultdict(list)

        for idx,(a,b) in enumerate(equations):
            adj_list[a].append((b,values[idx]))
            adj_list[b].append((a,1 / values[idx]))


        def bfs(start,end):
            if start not in adj_list or end not in adj_list:
                return -1  
            queue = deque()
            queue.append((start,1))
            visited = set()

            while queue:
                curr_node,curr_div = queue.popleft()
                if curr_node in visited:
                    continue
                visited.add(curr_node)
                if curr_node == end:
                    return curr_div

                for node,val in adj_list[curr_node]:
                    queue.append((node,curr_div * val))


            return -1

        return [bfs(start,end) for start,end in queries]