class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = set(list("qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM"))
        s = s.lower()
        left, right = 0,len(s)-1 

        while left < right:
            if s[left] != s[right]:
                if s[left] not in alpha:
                    left += 1
                    continue
                elif s[right] not in alpha:
                    right -= 1 
                    continue
                return False

            else:
                right -= 1 
                left += 1 

        return True 
        