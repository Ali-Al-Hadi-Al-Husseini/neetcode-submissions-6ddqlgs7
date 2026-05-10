class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.longest = ""
        self.s = s
        for idx in range(len(s)):
            print(idx)
            self.check_for_pal(idx,idx)

            self.check_for_pal(idx,idx+1)



        return self.longest

    
    def check_for_pal(self,left,right):

        while (left >= 0 and  right < len(self.s) ) and self.s[left] == self.s[right]:
            self.longest = max( self.longest,self.s[left:right+1],key= lambda x:len(x))
            left -= 1
            right +=1 
