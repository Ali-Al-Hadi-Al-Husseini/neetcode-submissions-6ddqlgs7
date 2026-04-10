class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        freq_s = get_freq(s)
        freq_t = get_freq(t)



        return is_anagram(s,freq_t) and is_anagram(t,freq_s)





def is_anagram(word,freq):

    for _char in word:
        if _char not in freq:
            return False
        
        if freq[_char] <= 0:
            return False


        freq[_char] -= 1  

    return True

def get_freq(word):
    freq = {}

    for _char in word:
        if _char not in freq:
            freq[_char] = 0

        freq[_char] += 1

    return freq




