from functools import cache

class Solution:
    def minSteps(self, n: int) -> int:
        
        @cache
        def helper(curr,clip):
            if curr == n :
                return 0
            if curr  > n :
                return float("inf")

            copy_paste = 2 + helper(curr *2,curr)
            if copy_paste != float("inf"):
                return copy_paste
            return 1 + helper(curr + clip,clip)
            
        return helper(1,1)