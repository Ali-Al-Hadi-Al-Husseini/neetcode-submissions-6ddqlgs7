class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        visited = set()
        heap = [(0,0,0)]
        steps = [[0,1],[1,0],[-1,0],[0,-1]]
        rows,cols = len(heights),len(heights[0])

        while heap :
            effort,r,c = heapq.heappop(heap)
            if (r,c) in visited:
                continue
            visited.add((r,c))

            if (r,c) == (rows-1,cols-1):
                return effort
            
            for rs,cs in steps:
                new_row , new_col = r + rs, c+ cs 
                if not (0 <= new_row < rows and 0 <= new_col < cols) :
                    continue
                
                new_effort = max(effort,abs(heights[r][c] - heights[r+rs][c+cs]))
                heapq.heappush(heap,(new_effort,r+rs,c+cs))
            
    

        return 0




    