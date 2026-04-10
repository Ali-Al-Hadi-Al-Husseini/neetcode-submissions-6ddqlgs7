class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = [[False for col in row  ] for row in board]

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "X" or visited[row][col]:
                    visited[row][col] = True 
                    continue
                is_surrounded, nodes = dfs(row,col,board,visited)
                if is_surrounded:
                    for node in nodes:
                        r, c = node
                        board[r][c] = "X"
        
        # return board


def dfs(row, col, board, visited):

    stack = [(row,col)]
    region = []
    is_surrounded = True
    while stack:
        row,col = stack.pop()
        neighbors = steps(row, col, board)

        for neigh in neighbors:
            r,c = neigh
            if visited[r][c]:
                continue
            if r == 0 or r == len(board) -1 or c == len(board[0]) -1  or c == 0:
                is_surrounded = False
            stack.append((r,c))
        if row == 0 or row == len(board) -1 or col == 0 or col == len(board[0]) -1:
            is_surrounded = False
        region.append((row,col))
        visited[row][col] = True
        

    return is_surrounded, region



def steps(row,col,board):
    stepp = [[0,1],[1,0],[-1,0],[0,-1]]
    found = []
    for step in stepp :
        new_row = step[0] + row 
        new_col = step[1] + col

        in_row = new_row < 0 or new_row >= len(board)
        in_col = new_col < 0 or new_col >= len(board[row])
        # print(in_row,in_col)
        not_in_bounds =  in_row or in_col 
        if not_in_bounds:
            # print(not_in_bounds)
            continue

        if board[new_row][new_col] == "X":
            continue
        
        found.append((new_row,new_col))
    # print(found)

    return found

