class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.memo = {}

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        all_sum = 0
        for row in range(row1,row2+1):
            row_sum = 0
            if (row,col1,col2) not in self.memo:
                for col in range(col1,col2+1):
                    row_sum += self.matrix[row][col]
                self.memo[(row,col1,col2)] = row_sum 
            else:
                row_sum = self.memo[(row,col1,col2)]

            all_sum += row_sum

        return all_sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)