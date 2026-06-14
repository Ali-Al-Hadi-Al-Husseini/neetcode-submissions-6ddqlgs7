class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = [0] * 26
        res = 0
        l,r = 0,0
        counter[ord(s[0]) - ord("A")] += 1
        while r < len(s):
            most_frequnt_char = max(counter)
            curr_str = s[l:r+1]

            if len(curr_str)- most_frequnt_char <=k:
                res = max(res,len(curr_str))
                r+=1
                if r < len(s):
                    counter[ord(s[r]) - ord("A")] += 1

            else:
                counter[ord(s[l]) - ord("A")] -= 1

                l+=1


        return res 