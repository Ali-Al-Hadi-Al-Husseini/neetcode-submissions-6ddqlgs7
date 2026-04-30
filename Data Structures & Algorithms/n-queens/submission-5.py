class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        grid = [["." for _ in range(n)] for _ in range(n)]
        used_boxes = [[0 for _ in range(n)] for _ in range(n)]
        grids = []

        def try_to_fill_grid(parent_row,n):
            if n == 0 :
                grids.append(["".join(row) for row in grid ])
                return

            
            for row in range(parent_row,len(grid)):
                for col in range(len(grid[0])):
                    if used_boxes[row][col] == 0 :
                        grid[row][col] = "Q"
                        mark_boxes(row,col,used_boxes)
                        try_to_fill_grid(row + 1,n-1)
                        un_mark_boxes(row,col,used_boxes)
                        grid[row][col] = "."
                        


        try_to_fill_grid(0,n)
        return grids

def mark_boxes(row,col,boxes):
    n = len(boxes)
    steps = [[1,1],[1,-1],[-1,1],[-1,-1]]
    for idx in range(n):
        boxes[row][idx] += 1
        boxes[idx][col] += 1
        
        for step in steps:
            new_row,new_col = row +(step[0] * idx), col + (step[1] * idx)


            if -1 < new_row < n and -1 < new_col < n:
                boxes[new_row][new_col] += 1
        

def un_mark_boxes(row,col,boxes):
    n = len(boxes)
    steps = [[1,1],[1,-1],[-1,1],[-1,-1]]
    for idx in range(n):
        boxes[row][idx] -= 1
        boxes[idx][col] -= 1
        
        for step in steps:
            new_row,new_col = row +(step[0] * idx), col + (step[1] * idx)


            if -1 < new_row < n and -1 < new_col < n:
                boxes[new_row][new_col] -= 1
        

        



