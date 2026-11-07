class Solution:
    def minSteps(self, n: int) -> int:

        def helper(curr,clip):
            if curr == n :
                return 0
            if curr  > n :
                return float("inf")

            copy_paste = 2 + helper(curr *2,curr)
            if copy_paste != float("inf"):
                return copy_paste
            paste = 1 + helper(curr + clip,clip)
            return paste
            
        
        return helper(1,1)