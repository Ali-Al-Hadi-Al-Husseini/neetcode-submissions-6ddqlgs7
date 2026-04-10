class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = [[0 for _ in matrix] for _ in matrix[0]]
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                res[col][row] = matrix[row][col]

        return res 