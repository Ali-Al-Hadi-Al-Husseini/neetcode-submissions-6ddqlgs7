class Solution:
    def validPalindrome(self,s: str) -> bool:
        l,r = 0,len(s) -1 
        check_point = None
        
        while l < r :
            if s[l] == s[r]:
                l+= 1
                r -=1 
            elif check_point is None :
                check_point = (l,r)
                r -= 1 

            elif check_point != "failed":
                l,r = check_point
                l += 1
                check_point = "failed"
            else:

                return False

        return True