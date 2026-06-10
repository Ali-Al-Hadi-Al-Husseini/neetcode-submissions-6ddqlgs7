class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = {}
        n,m = len(obstacleGrid),len(obstacleGrid[0])

        def dfs(r,c):
            if r == n or c == m or obstacleGrid[r][c] == 1:
                return 0
            if (r,c) == (n-1,m-1):
                return 1
            if (r,c) in memo:
                return memo[(r,c)]

            paths = 0
            paths += dfs(r+1, c)
            paths += dfs(r, c+1)
            memo[(r,c)] = paths 
            return paths


        return dfs(0,0)