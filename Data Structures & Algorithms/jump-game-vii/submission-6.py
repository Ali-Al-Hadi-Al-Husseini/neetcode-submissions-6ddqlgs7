class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        
        memo = set()


        def jump(i):
            if i in memo  or s[i] == "1":
                return False
            if i == len(s) -1 :
                return True


            for j in range(min(i+maxJump, len(s)-1),i+minJump -1 , -1 ):
                if s[j] == "0"  and jump(j) : return True
                memo.add(j)

            return False


        return jump(0)