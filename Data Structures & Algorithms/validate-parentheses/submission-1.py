class Solution:
    def isValid(self, s: str) -> bool:
        open_ = {"{","[","("} 
        close = {"}":"{","]": "[",')' :"("}
        stack = []

        for paren in s:
            if paren in open_:
                stack.append(paren)
            elif paren in close:
                if len(stack) == 0:
                    return False 
                    
                last_open = stack.pop()
                if last_open != close[paren]:
                    return False
        
        return len(stack) == 0 
            