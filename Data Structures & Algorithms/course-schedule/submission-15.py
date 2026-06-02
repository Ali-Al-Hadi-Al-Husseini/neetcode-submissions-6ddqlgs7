class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #topological sort khans
        adj_list = [[] for _ in range(numCourses)]
        dependcies = [0 for _ in range(numCourses)]

        for preq,course in prerequisites:
            adj_list[preq].append(course)
            dependcies[course] += 1 



        def bfs():
            queue = deque()
            visited = set()
            for course,dep in enumerate(dependcies):
                if dep == 0 :
                    queue.append(course)

            while queue:
                curr_crs = queue.popleft() 
                if curr_crs in visited:
                    continue
                visited.add(curr_crs)
                for crs in adj_list[curr_crs]:
                    dependcies[crs] -= 1 
                    if  dependcies[crs] <= 0  :
                        queue.append(crs)
                        dependcies[crs] = -1

            
            for dep in dependcies:
                if dep > 0 :
                    return False
            return True

        return bfs()