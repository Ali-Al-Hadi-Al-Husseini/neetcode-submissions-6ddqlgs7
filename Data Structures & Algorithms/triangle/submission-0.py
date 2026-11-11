from functools import cache 

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        @cache
        def helper(r,c):
            if c >= len(triangle[r])  or c < 0  or r >= len(triangle):
                return float("inf")
            if r == len(triangle) - 1 :
                return triangle[r][c]


            return  triangle[r][c] + min(helper(r+1,c),helper(r+1,c+1))


        return helper(0,0)

            