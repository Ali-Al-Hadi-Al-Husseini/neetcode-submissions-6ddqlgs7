import sys 
sys.setrecursionlimit(2000)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_sub_string = [""]
        memo = set()

        def helper(start,end):
            if start > end:
                return
            if (start,end) in memo:
                return

            if is_palindrome(s[start:end]):
                longest_sub_string[0] = max(s[start:end],longest_sub_string[0],key= lambda x:len(x))


            helper(start+1,end)
            helper(start, end - 1)
            memo.add((start,end))

        
        helper(0,len(s))
        return longest_sub_string[0]

def is_palindrome(string):
    return string == string[::-1]