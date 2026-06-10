class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backTrack(closing, opening):
            if closing == opening == n :
                res.append("".join(stack))
                return 

            if opening < n:
                stack.append("(")
                backTrack(closing,opening+1)
                stack.pop()
            if closing < opening :
                stack.append(")")
                backTrack(closing+1,opening)
                stack.pop()


        
        backTrack(0,0)
        return res 