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
        idx = 0
        while idx < len(s):
            _char = s[idx]

            if next_is_bigger(idx,s):
                res += (roman_to_int[s[idx+1]] - roman_to_int[_char])
                idx += 1 
            elif _char in roman_to_int:
                res += roman_to_int[_char]
            idx += 1 

        return res 

def next_is_bigger(idx,s):
    if idx + 1 >= len(s):return False

    if roman_to_int[s[idx]] < roman_to_int[s[idx +1]]:
        return True
    return False  