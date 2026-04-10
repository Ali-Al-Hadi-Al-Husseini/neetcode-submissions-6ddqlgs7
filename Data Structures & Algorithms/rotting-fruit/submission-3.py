class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = collections.deque()
        empty_count = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 2:
                    queue.append((row,col,0))
                elif grid[row][col] == 0:
                    empty_count += 1
        
        rotten,time_needed = bfs(queue,grid)
        rotted_all_fresh = rotten + empty_count == (len(grid)*len(grid[0]))
        return time_needed if rotted_all_fresh else -1 


def bfs(queue,grid):
    visited = set()
    time_needed = -1 
    steps = [[1,0],[0,1],[-1,0],[0,-1]]
    max_time = 0

    while queue:
        row,col,time = queue.popleft()
        if (row,col) in visited:
            continue

        for step in steps:
            new_row = row + step[0]
            new_col = col + step[1]
            curr_time = 1 + time

            not_in_bounds = 0 > new_row or new_row >= len(grid) or 0 > new_col or new_col >= len(grid[row])

            if (new_row,new_col) in visited or not_in_bounds:
                continue 

            if grid[new_row][new_col] == 2 or grid[new_row][new_col] == 0:
                continue 

            max_time = max(max_time,curr_time)
            queue.append((new_row,new_col,curr_time ))

        visited.add((row,col))
    return len(visited), max_time
            





