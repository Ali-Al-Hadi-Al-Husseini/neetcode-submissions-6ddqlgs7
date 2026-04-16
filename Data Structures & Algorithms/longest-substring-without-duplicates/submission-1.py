class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        repeated_chars = {}
        max_size = 0
        curr_size = 0
        i = 0


        while i < len(s):

            if s[i] in repeated_chars:
                i = repeated_chars[s[i]] + 1 
                repeated_chars = {}
                curr_size = 0 

            curr_size += 1 
            repeated_chars[s[i]] = i
            max_size = max(max_size, curr_size)
            i += 1

        
        return max_size