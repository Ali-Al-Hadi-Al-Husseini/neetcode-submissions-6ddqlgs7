class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}


        def dfs(row,col):
            if (row,col) in memo:
                return memo[(row,col)]

            steps = [[1,0],[0,1],[-1,0],[0,-1]]

            curr_longest_path = 0
            for r,c in steps:
                new_row ,new_col= row+r , col +c
                in_bounds =  (-1 < new_row < len(matrix)) and (-1 < new_col < len(matrix[0]))
                if not in_bounds or matrix[row][col]  >= matrix[new_row][new_col] :
                    continue

                curr_longest_path = max(curr_longest_path,dfs(new_row,new_col)+1)

            memo[(row,col)] = curr_longest_path 

            return curr_longest_path  
        
        longest_path = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                longest_path = max(longest_path,dfs(r,c))

        return longest_path + 1