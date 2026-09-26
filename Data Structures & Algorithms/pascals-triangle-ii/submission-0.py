class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = [1]


        for row in range(2,rowIndex+2):
            new = [1] * row
            for i in range(1,row-1):
                new[i] = triangle[i-1] + triangle[i]

            triangle = new

        return triangle