class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        elvations = [[0 for _ in range(n)] for _ in range(n)]

        min_heap = [(grid[0][0], 0,0)]
        visited = set()

        while min_heap:
            curr_elvation,curr_row,curr_col = heapq.heappop(min_heap)
            if (curr_row,curr_col) in visited:
                continue
            if (curr_row,curr_col) == (n-1,n-1):
                return curr_elvation

            visited.add((curr_row,curr_col))
            steps = [(0,1),(1,0),(-1,0),(0,-1)]

            for step in steps:
                row,col = curr_row +step[0], curr_col +step[1]
                if  (row,col) in visited or not in_bound(row,col,n):
                    continue

                if elvations[row][col] <= grid[row][col]:
                    heapq.heappush(min_heap,(max(curr_elvation, grid[row][col]),row,col))
        return elvations[n-1][n-1]


def in_bound(row,col,n):
    return 0 <= row < n and 0 <= col < n