class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 1 : return matrix[0]
        m,n = len(matrix) , len(matrix[0])
        result = []
        next_diretion= {(0,1):(1,0),
                        (1,0):(0,-1),
                        (0,-1):(-1,0),
                        (-1,0): (0,1)}
        row, col = 0 , 0
        direction = (0,1)
    
        while len(result) < m * n :
            result.append(matrix[row][col])
            
            if should_change_direction(row,col,matrix,direction):
                direction = next_diretion[direction]

            matrix[row][col] = None
            row,col = row + direction[0], col + direction[1]

        return result




def should_change_direction(row,col,matrix,direction):

    if col == len(matrix[0]) -1  and ( row ==0 or row == len(matrix) -1) :
        return True
    if row == len(matrix) - 1 and col == 0:
        return True
    new_row,new_col = row + direction[0], col + direction[1]
    if matrix[new_row][new_col] == None:
        return True
    return False 
