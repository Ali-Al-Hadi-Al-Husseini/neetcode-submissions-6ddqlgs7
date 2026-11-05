class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid),len(grid[0])
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]

        def dfs(row,col):
            if grid[row][col] == 0 or visited[row][col]:
                return 0
            visited[row][col] = True
            steps = [(1,0),(0,1),(-1,0),(0,-1)]
            curr_max = 0

            for rs,cs in steps:
                r = rs + row
                c = cs + col 

                in_bounds = ROWS > r >= 0 and COLS > c >= 0
                if not in_bounds:
                    continue

                curr_max  = max(curr_max,dfs(r,c))

            visited[row][col] = False
            return grid[row][col] + curr_max

            
        return max([dfs(row,col) for col in range(COLS) for row in range(ROWS)])
