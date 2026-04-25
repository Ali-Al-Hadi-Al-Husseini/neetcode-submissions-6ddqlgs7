class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        start, end = 0, len(s1)

        while end <= len(s2):
            print(s2[start:end])
            if is_same(s1,s2[start:end]):
                return True

            start += 1 
            end += 1 
        
        return False



def is_same(s1, s2):
    s1_arr = [0] * 26
    s2_arr = [0] * 26

    for idx in range(len(s1)):
        s1_arr[ord(s1[idx]) - ord("a")] += 1 
        s2_arr[ord(s2[idx]) - ord("a")] += 1 


    return s1_arr == s2_arr
