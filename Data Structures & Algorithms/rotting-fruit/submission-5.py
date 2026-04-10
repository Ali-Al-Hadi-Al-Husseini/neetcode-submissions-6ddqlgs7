class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time,fresh = 0,0

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    fresh +=1



        steps = [[1,0],[0,1],[-1,0],[0,-1]]
        flag = True
        while fresh > 0:

            for row in range(len(grid)):
                for col in range(len(grid[row])):
                    if grid[row][col] != 2:
                        continue

                    for rd,cd in steps:
                        print("hola")
                        new_row,new_col = row+rd, col + cd 
                        
                        not_in_bound = 0 > new_row or new_row >= len(grid) or new_col >= len(grid[row]) or 0 > new_col
                        if not_in_bound :
                            continue
                        if grid[new_row][new_col] != 1 :
                            continue
                        
                        print("amigo")
                        fresh -= 1 
                        grid[new_row][new_col] = 3 
                        flag = False

            if flag:
                return -1

            for row in range(len(grid)):
                for col in range(len(grid[row])):
                    if grid[row][col] == 3:
                        grid[row][col] = 2 
                        
            flag = True
            time +=1 

        return time
