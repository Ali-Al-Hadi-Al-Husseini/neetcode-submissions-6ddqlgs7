
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        visited_atalantic = set()
        visited_pacfic= set()

        def dfs(r,c,visited):
            visited.add((r,c))

            for neigh in get_neighbors(r,c, heights):
                row,col = neigh
                if neigh in visited or heights[row][col] < heights[r][c]:
                    continue

                visited.add(neigh)
                has_path = dfs(row,col,visited)

        for row in range(len(heights)):
            dfs(row,0,visited_atalantic)
            dfs(row,len(heights[0]) -1,visited_pacfic)
        
        for col in range(len(heights[0])):
            dfs(0,col,visited_atalantic)
            dfs(len(heights) -1,col,visited_pacfic )
        

        result = []

        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if (r,c) in visited_atalantic   and (r,c) in visited_pacfic:
                    result.append([r,c])

        return result 

        
            
def get_neighbors(r,c, heights):
    steps = [[0,1],[1,0],[-1,0],[0,-1]]
    res = []

    for step in steps:
        new_row = r + step[0]
        new_col = c + step[1]

        if in_bound(new_row, new_col, heights):
            res.append((new_row,new_col))

    return res

def in_bound(r,c,heights):
    if r < 0 or c < 0 :return False
    if r >= len(heights) or c >= len(heights[0]): return False

    return True

