class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        max_area = 0

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 0 or (row,col) in visited:
                    continue
                
                curr_size = get_island_size(row,col,grid,visited)
                max_area = max(max_area,curr_size )
                


        return max_area


def get_island_size(row, col, grid,visited):
    queue = [(row,col)]
    steps =[[0,1],
            [1,0],
            [-1,0],
            [0,-1]]

    island_area = 0

    while queue:
        curr_row, curr_col = queue.pop()

        if (curr_row,curr_col) in visited:
            continue
        
        
        for step in steps:
            new_row,new_col = curr_row + step[0], curr_col +step[1]

            not_in_bounds =  0 > new_row or new_row >= len(grid) or  0 > new_col or new_col >= len(grid[curr_row])   

            if not_in_bounds:
                continue
            if (new_row,new_col) in visited or grid[new_row][new_col] == 0:
                continue
            
            queue.append((new_row,new_col))

        island_area += 1 
        visited.add((curr_row,curr_col))

    return island_area

