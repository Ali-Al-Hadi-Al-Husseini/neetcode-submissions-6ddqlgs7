class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        cost = [float("inf") for _ in range(n+1)] 
        cost[n-1] = 0

        for r in range(m-1,-1,-1):
            for c in range(n-1,-1,-1):
                cost[c] = grid[r][c] + min(cost[c],cost[c+1])


        return cost[0]
