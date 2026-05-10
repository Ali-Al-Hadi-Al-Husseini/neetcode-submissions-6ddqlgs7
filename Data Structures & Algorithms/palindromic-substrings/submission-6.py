class Solution:
    def countSubstrings(self, s: str) -> int:
        self.count = 0
        self.s = s

        for idx in range(len(s)):
            self.check_for_pal(idx,idx)
            self.check_for_pal(idx,idx+1)

        return self.count



    def check_for_pal(self,left,right):

        while left >= 0 and right < len(self.s) and self.s[left] == self.s[right]:
            self.count +=1
            left -= 1
            right +=1