class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []

        def helper(idx):
            if idx >= len(s):
                res.append(curr[:])
                return 

            for j in range(idx,len(s)):
                if is_palindrome(s[idx:j+1]):
                    curr.append(s[idx:j+1])
                    helper(j+1)
                    curr.pop()


        helper(0)

        return res 





def is_palindrome(string):
    left,right = 0 ,len(string) -1

    while left <= right:
        if string[left] != string[right]:
            return False
        left+= 1
        right -=1

    return True