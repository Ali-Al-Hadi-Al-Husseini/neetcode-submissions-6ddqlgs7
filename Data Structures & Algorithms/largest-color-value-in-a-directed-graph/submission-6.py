class Node:
    def __init__(self,color,idx):
        self.clr = color
        self.idx = idx 
        self.edg = []

    def tp(self):
        return (self.idx,self.clr)

import sys 
sys.setrecursionlimit(10000000)
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        adj_list = [ Node(colr,idx) for idx,colr in enumerate(colors)]


        for x,y in edges:
            if x == y :
                return -1
            adj_list[x].edg.append(y)

        def dfs(curr,visited,colrs,path):
            if curr.tp() in path:
                return [0 for _ in range(26)] , True
            if curr in visited:
                return [-1 for _ in range(26)], False

            visited.add(curr.tp())
            path.add(curr.tp())
            results = []
            for edg in curr.edg:
                res, has_cycle = dfs(adj_list[edg],visited,colrs[:],path)
                if has_cycle:
                    return res, True 
                results.append(res)

            path.remove(curr.tp())
            for res in results:
                for i in range(len(res)):
                    colrs[i] = max(colrs[i],res[i])
            colrs[ord('a') - ord(curr.clr)] += 1 
            return colrs, False
        max_clr = 0

        for node in adj_list:
            res,has_cycle = dfs(node,set(),[0 for _ in range(26)],set())
            if has_cycle:
                return -1

            max_clr = max(max(res),max_clr)
            if max_clr == len(colors):
                return max_clr

        return max_clr


         
