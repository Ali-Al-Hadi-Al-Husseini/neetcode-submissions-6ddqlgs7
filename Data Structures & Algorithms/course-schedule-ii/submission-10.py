class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = [[] for _ in range(numCourses)]

        for crs,req in prerequisites:
            adj_list[crs].append(req)
            
        visited = set()
        result = []

        def dfs(crs,curr_set):
            if crs is None :
                return 
            if crs in visited:
                return 
            
            visited.add(crs)
            curr_set.add(crs)
            for req in adj_list[crs]:
                if req in curr_set:
                    print("has cycle")
                    return 
                dfs(req,curr_set)
            curr_set.remove(crs)

            
            result.append(crs)

        for crs in range(numCourses):
            if crs not in visited:
                dfs(crs,set())
        print(adj_list)

        return result if len(result) == numCourses else []