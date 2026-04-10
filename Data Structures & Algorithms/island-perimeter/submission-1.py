class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])) :
                if grid[row][col] == 1 :
                    res += 4
                    if row and grid[row-1][col]:
                        res -=2
                    if col and grid[row][col-1]:
                        res -=2
                    


        return res 