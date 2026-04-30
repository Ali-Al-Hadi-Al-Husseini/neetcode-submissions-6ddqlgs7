class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        basic_grid = [["." for _ in range(n)] for _ in range(n)]
        basic_used_boxes = [[False for _ in range(n)] for _ in range(n)]
        grids = []

        def try_to_fill_grid(row,n,curr_grid,used_boxes):
            if n == 0 :
                grids.append(["".join(row) for row in curr_grid ])
                return

            
            for row in range(row,len(curr_grid)):
                for col in range(len(curr_grid[0])):
                    if not used_boxes[row][col]:
                        new_grid= [row[:] for row in curr_grid]
                        new_grid[row][col] = "Q"
                        new_used_boxes = [row[:] for row in used_boxes]
                        mark_boxes(row,col,new_used_boxes)
                        try_to_fill_grid(row + 1,n-1,new_grid,new_used_boxes)
                        


        try_to_fill_grid(0,n,basic_grid[:],basic_used_boxes[:])
        return grids

def mark_boxes(row,col,boxes):
    n = len(boxes)
    steps = [[1,1],[1,-1],[-1,1],[-1,-1]]
    for idx in range(n):
        boxes[row][idx] = True
        boxes[idx][col] = True
        
        for step in steps:
            new_row,new_col = row +(step[0] * idx), col + (step[1] * idx)


            if -1 < new_row < n and -1 < new_col < n:
                boxes[new_row][new_col] = True
        

    



