class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix) -1, len(matrix[0]) -1 
        left, right = (0,0), (rows,cols)

        while is_smaller(left, right):

            mid = calculate_mid(left,right)            
            if matrix[mid[0]][mid[1]] > target:
                
                if mid[1] > 0:
                    right = (mid[0],mid[1] -1)
                elif mid[0] > 0:
                    right = (mid[0] -1, cols)
                else:
                    break
            elif matrix[mid[0]][mid[1]] < target:

                if mid[1] < cols :
                    left = (mid[0],mid[1] +1)

                elif mid[0] < rows:
                    left = (mid[0] +1, 0)

                else:
                    break

            else:
                return True


        return False


def is_smaller(left, right):
    if left[0] < right[0]: return True
    if left[0] > right[0]: return False
    return left[1] <= right[1]


def calculate_mid( left,right):
    return (((left[0] + right[0]) // 2),( right[1] + left[1] // 2))