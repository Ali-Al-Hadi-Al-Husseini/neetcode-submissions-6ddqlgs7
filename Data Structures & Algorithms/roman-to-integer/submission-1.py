roman_to_int =  {'I': 1,
                'V':5,
                'X':10,
                'L':50,
                'C':100,
                'D':500,
                'M':1000}

class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0

        for idx in range(len(s)):
            if next_is_bigger(idx,s):
                res -=roman_to_int[s[idx]]
            else:
                res += roman_to_int[s[idx]]

        return res 

def next_is_bigger(idx,s):
    return idx +1 < len(s) and roman_to_int[s[idx]] < roman_to_int[s[idx +1]]