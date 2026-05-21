class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj_list = [[] for _ in range(numCourses)]

        for preq,course in prerequisites:
            adj_list[preq].append( course)
        

        def is_child_of(parent,possible_child):
            queue = deque()
            queue.append(parent)
            visited = set()
            while queue:
                curr_node = queue.popleft()
                if curr_node == possible_child:
                    return True
                if curr_node in visited:
                    continue
                visited.add(curr_node)
                for child in adj_list[curr_node]:
                    queue.append(child)

            return False
        results = []

        for u,v in queries:
            if is_child_of(u,v):
                results.append(True)
            else:
                results.append(False)

        return results