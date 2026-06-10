class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n,m = len(obstacleGrid),len(obstacleGrid[0])
        memo = {(n-1,m-1) : 1}

        def dfs(r,c):
            if r == n or c == m or obstacleGrid[r][c] == 1:
                return 0
            if (r,c) in memo:
                return memo[(r,c)]

            memo[(r,c)] = dfs(r, c+1) + dfs(r+1, c) 
            return memo[(r,c)]


        return dfs(0,0)