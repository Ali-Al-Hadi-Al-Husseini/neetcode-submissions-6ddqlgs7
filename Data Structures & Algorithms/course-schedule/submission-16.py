class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #topological sort khans
        adj_list = [[] for _ in range(numCourses)]
        dependcies = [0 for _ in range(numCourses)]

        for course,preq in prerequisites:
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
                if dependcies[curr_crs] == -1 :
                    continue
                dependcies[curr_crs] = -1
                visited.add(curr_crs)
                for crs in adj_list[curr_crs]:
                    dependcies[crs] -= 1 
                    if  dependcies[crs] <= 0  :
                        queue.append(crs)

            
            for dep in dependcies:
                if dep > 0 :
                    return False
            return True

        return bfs()