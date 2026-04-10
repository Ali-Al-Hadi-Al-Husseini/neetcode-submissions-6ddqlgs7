class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647
        visited = set()
        

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == inf :
                    bfs(row,col,grid)



def bfs(row,col,grid):
    visited = set()
    queue = [(row,col,1)]
    steps = [[1,0],[0,1],[-1,0],[0,-1]]

    while queue:
        curr_row,curr_col,curr_distance = queue.pop(0)
        if (curr_row,curr_col) in visited:
            continue

        for step in steps:
            new_row = curr_row + step[0]
            new_col = curr_col + step[1]

            not_in_bounds = 0 > new_row or new_row >= len(grid) or 0 > new_col or new_col >=len(grid[new_row])

            if not_in_bounds :
                continue
            if grid[new_row][new_col] == -1:
                continue
            if grid[new_row][new_col] == 0:
                grid[row][col] = min(curr_distance  , grid[row][col]) 
                

            queue.append((new_row,new_col,curr_distance+1))
        visited.add((curr_row,curr_col ))

        

