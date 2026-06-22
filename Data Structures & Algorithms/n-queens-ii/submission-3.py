class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        diagnols_1 = set()
        diagnols_2 = set()

        solutions = [0]
        def fill(row):
            if row == n:
                solutions[0] += 1
                return 

            for col in range(n):
                if col in cols or (row+col) in diagnols_1 or (row-col) in diagnols_2:
                    continue
                
                cols.add(col)
                diagnols_1.add((row + col)) 
                diagnols_2.add((row - col)) 

                fill(row+1)

                cols.remove(col)
                diagnols_1.remove((row + col)) 
                diagnols_2.remove((row - col)) 




        fill(0)
        return solutions[0]

