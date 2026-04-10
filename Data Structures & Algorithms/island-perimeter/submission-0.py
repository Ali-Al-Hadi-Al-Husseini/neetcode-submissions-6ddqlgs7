class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        for row in range(len(grid)):
            for col in range(len(grid[row])) :
                if grid[row][col] == 1 :
                    perimertet= find_island_permirter(row,col,grid)
                    break 


        return perimertet



def find_island_permirter(row,col, grid):
    visited = set()
    total_perimiter = 0
    stack = [(row,col)]

    while stack:
        row,col = stack.pop()
        if(row,col) in visited:
            continue
        sides, curr_perimeter= check_four_sides(row,col,grid)

        total_perimiter += curr_perimeter
        stack.extend(sides)
        visited.add((row,col))

    return total_perimiter




def check_four_sides(row,col,grid):
    steps = [[0,1],[1,0],[-1,0],[0,-1]]
    perimeter = 0
    sides = []
    for step in steps:
        new_row = row + step[0]
        new_col = col + step[1]

        col_not_in_bound= new_col >= len(grid[0]) or new_col <0  
        row_not_in_bound= new_row >= len(grid) or new_row <0  

        if row_not_in_bound or col_not_in_bound :
            perimeter += 1
            continue 
        if grid[new_row][new_col] == 1:
            sides.append((new_row,new_col))
        else:
            perimeter+= 1

    return sides,perimeter






