class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palind = ""

        for start in range(len(s)):
            for end in range(start,len(s)+1):
                if is_palindrome(s[start:end]): 
                    longest_palind =  max(s[start:end],longest_palind,key= lambda x:len(x))


        return longest_palind

def is_palindrome(string):
    return string == string[::-1]