class Solution:
    def checkValidString(self, s: str) -> bool:
        paren = []
        stars = []

        for idx,_chr in enumerate(s):
            if _chr == "(":
                paren.append(idx)
            elif _chr == "*":
                stars.append(idx)
            else:
                if not paren and not stars:
                    return False

                if paren:
                    paren.pop()
                else:
                    stars.pop()
        while paren and stars:
            if paren.pop() > stars.pop():
                return False

        return not paren