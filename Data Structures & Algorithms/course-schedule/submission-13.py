class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i:[] for i in range(numCourses)}
        

        for preq in prerequisites:
            adj_list[preq[0]].append(preq[1])


        visiting = set()

        for c in range(numCourses):
            if not dfs(c,visiting, adj_list):
                return False
        return True 



def dfs(curr, visiting, adj_list):
    if curr in visiting:
        return False
    if len(adj_list[curr]) == 0:
        return True 

    visiting.add(curr)
    for preq in adj_list[curr]:
        if not dfs(preq,visiting,adj_list):
            return False 
    visiting.remove(curr)
    adj_list[curr] = []

    return True 