class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS , COLS = len(matrix), len(matrix[0])
        left, right = 0 , (ROWS * COLS ) - 1 


        while left <= right:
            mid = (left + right) // 2

            row,col = convert_to_non_linear(mid, COLS)

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = mid - 1 

            else:
                left = mid  + 1
        return False

def convert_to_non_linear(idx, COLS):
    return idx // COLS , idx % COLS