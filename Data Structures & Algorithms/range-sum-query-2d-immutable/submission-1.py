class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix 
        self.sums = [[val for val in matrix[idx]] for idx in range(len(matrix))]

        for  row in range(len(matrix)):
            for col in range(1,len(matrix[0])):
                self.sums[row][col] += self.sums[row][col-1]



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        curr_sum = 0

        for idx in range(row1,row2+1):
            row = self.sums[idx]
            left_col_sum = row[col1-1]  if col1 > 0 else 0
            curr_sum += row[col2] - left_col_sum

        return curr_sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)