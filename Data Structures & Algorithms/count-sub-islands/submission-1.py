class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows,cols = len(grid1), len(grid1[0])
        island_count = 0 

        def is_sub_island(row,col):
            stack = [(row,col)]
            visiting = set()
            visiting.add((row,col))

            island= True
            while stack :
                r,c = stack.pop()
                if not ( grid2[r][c] == grid1[r][c]== 1):
                    island = False
                grid2[r][c]= 0
                visiting.remove((r,c))

                steps = [(0,1),(1,0),(-1,0),(0,-1)]

                for step in steps:
                    new_r = r + step[0]
                    new_c = c + step[1]

                    in_bound =  rows > new_r >= 0 and cols > new_c >= 0 
                    if in_bound and grid2[new_r][new_c] == 1 and (new_r,new_c) not in visiting:
                        stack.append((new_r,new_c))
                        visiting.add((new_r,new_c))

            return island

        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] == 0:
                    continue
                
                if is_sub_island(r,c):
                    island_count +=1
                

        return island_count