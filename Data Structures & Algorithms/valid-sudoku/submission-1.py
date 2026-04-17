class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in board:
            row_set = set()
            for num in row :
                if num == ".":
                    continue
                if num in row_set:
                    return False
                row_set.add(num)


        for row in range(len(board)):
            col_set = set()
            for col in range(len(board[0])) :
                num = board[col][row]
                if num == ".":
                    continue
                if num in col_set:
                    return False
                col_set.add(num)

        for row in range(len(board) // 3):
            for col in range(len(board[0]) // 3):
                box_set = set()
                for r,c in get_box(row,col):
                    num = board[r][c]
                    if num == ".":
                        continue
                    if num in box_set:
                        return False
                    box_set.add(num)
        
        return True


def get_box(row,col):
    row *=  3
    col *=  3
    indices = []

    for r in range(row,row+3):
        for c in range(col, col + 3):
            indices.append((r,c))

    return indices





