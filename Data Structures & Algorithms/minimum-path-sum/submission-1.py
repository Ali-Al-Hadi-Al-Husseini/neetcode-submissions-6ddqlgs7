class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        cost = [[-1 for _ in range(n)] for _ in range(m)]




        def get_cost(r,c):
            if r >= m or c >= n:
                return float("inf")
            if r== m -1 and c == n -1 :
                return grid[r][c]
            if cost[r][c] >= 0:
                return cost[r][c]

            cost[r][c] = grid[r][c] +  min (get_cost(r+1,c),get_cost(r,c+1))

            return  cost[r][c] 


        return get_cost(0,0)
