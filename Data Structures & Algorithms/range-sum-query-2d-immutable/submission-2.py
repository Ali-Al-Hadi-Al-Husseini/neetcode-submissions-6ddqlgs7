class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.sums = [[val for val in row] for row in matrix]

        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                row_sum = self.sums[row-1 ][col] if row -1 >= 0 else 0
                col_sum = self.sums[row ][col-1] if col -1 >= 0 else 0
                corner = self.sums[row-1][col -1] if (col-1 >=0 and row -1 >= 0) else 0
                self.sums[row][col] += row_sum + col_sum - corner
        
        for row in self.sums:
            print(row)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        curr_rectangle = self.sums[row2][col2]
        corner = self.sums[row1-1][col1 -1] if (col1-1 >=0 and row1 -1 >= 0) else 0
        row_sum = self.sums[row1-1][col2] if (row1 -1 >= 0) else 0
        col_sum = self.sums[row2][col1-1] if col1 -1 >= 0 else 0

        return curr_rectangle - row_sum - col_sum + corner

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)