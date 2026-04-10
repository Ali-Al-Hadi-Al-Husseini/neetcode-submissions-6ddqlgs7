class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i:[] for i in range(numCourses)}


        for preq in prerequisites:
            adj_list[preq[0]].append(preq[1])


        for i in range(numCourses):
            stack = adj_list[i]
            while stack:
                curr = stack.pop()
                if curr == i:
                    return False
                
                stack.extend(adj_list[curr])

        return True 