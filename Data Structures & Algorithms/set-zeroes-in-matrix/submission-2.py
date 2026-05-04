class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] != 0 :
                    continue
                zeroing(row,col,matrix)

    


        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] != -1:
                    continue
                matrix[row][col] = 0



        


def zeroing(row,col,matrix):
    for c in range(len(matrix[0])):
        if  matrix[row][c] == 0:
            continue
        matrix[row][c] = -1  
    for r in range(len(matrix)):
        if  matrix[r][col] == 0:
            continue
        matrix[r][col] = -1

