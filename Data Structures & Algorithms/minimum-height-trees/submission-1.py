class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        heights = [[] for _ in range(n+1)]
        adj_list= defaultdict(list)

        for v,e in edges:
            adj_list[v].append(e) 
            adj_list[e].append(v)

        def dfs(root,parent):
            if root is None:
                return 0
            
            curr_max = 0
            for child in adj_list[root]:
                if child == parent : continue 
                curr_max = max(curr_max, dfs(child,root))

            return curr_max +1 

        for i in range(n):
            heights[dfs(i,None)].append(i)



        for height in heights:
            if len(height) > 0 :
                return height
        
        return []