class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_preq = [[] for _ in range(numCourses) ]

        for preq in prerequisites:
            course_preq[preq[0]].append(preq[1])

        visited = set()
        cycle = set()
        path = []

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True

            cycle.add(course)
            for preq in course_preq[course]:
                if not dfs(preq):
                    return False

            cycle.remove(course)
            visited.add(course)
            path.append(course)
            return True 

        for course in range(numCourses):
            if not dfs(course):
                return []

        return path 
            
            