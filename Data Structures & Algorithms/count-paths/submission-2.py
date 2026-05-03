class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        memo = {(m-1,n-1):1}

        def count_paths(row,col):
            if (row >= m or col >= n ):
                return  0
            if (row,col) in memo:
                return memo[(row,col)]
            

            memo[(row,col)] = count_paths(row+1,col) + count_paths(row,col+1)
            return memo[(row,col)]
            

        
        return count_paths(0,0)