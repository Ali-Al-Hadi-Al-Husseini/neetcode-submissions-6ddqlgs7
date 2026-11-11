from functools import cache 

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        @cache
        def helper(r,c):
            if  r >= len(triangle):
                return 0
            return  triangle[r][c] + min(helper(r+1,c),helper(r+1,c+1))

        return helper(0,0)

            