class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        island_count= 0

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "0" or  (row,col) in visited:
                    continue

                print(visited)
                island_count += 1
                dfs(row,col ,grid,visited)

        return island_count

def dfs(start_row,start_col ,grid,visited):
    steps =[    [0,1],
                [1,0],
                [-1,0],
                [0,-1]
    ]
    stack = [(start_row,start_col)]
    while stack:
        row,col = stack.pop(0) 
        if (row,col) in visited:
            continue

        for step in steps:
            new_row = step[0] + row
            new_col = step[1] + col 
            
            
            if not(len(grid) > new_row >= 0 and len(grid[0]) > new_col >=0):
                continue 

            island = grid[new_row][new_col]
            if island == '0' or (new_row,new_col) in visited:
                continue
            stack.append((new_row,new_col))

        visited.add((row,col))




