class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        cost = [[float("inf") for _ in range(n+1)] for _ in range(m+1)]

        cost[m-1][n] = 0


        for r in range(m-1,-1,-1):
            for c in range(n-1,-1,-1):
                cost[r][c] = grid[r][c] + min(cost[r+1][c],cost[r][c+1])

        print(cost)
        return cost[0][0]
