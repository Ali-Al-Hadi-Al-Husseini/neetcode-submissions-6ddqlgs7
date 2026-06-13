import sys
sys.setrecursionlimit(2000)

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        memo = set()
        t_freq = defaultdict(int)
        s_freq = defaultdict(int)
        for _chr in t:
            t_freq[_chr] += 1 
        for _chr in s:
            s_freq[_chr] += 1 

        min_size = s
        
        def helper(l,r,freq):
            if l > r or (l,r) in memo:
                return 

            nonlocal min_size
            if has_chrs(freq,t_freq):
                min_size= min (s[l:r+1] , min_size , key=lambda x:len(x))
            memo.add((l,r))
            
            freq[s[l]] -= 1
            helper(l+1,r,freq)
            freq[s[l]] += 1

            freq[s[r]] -= 1
            helper(l,r-1,freq)
            freq[s[r]] += 1

        helper(0,len(s) - 1,s_freq)
        if min_size == s:
            return s if has_chrs(s_freq,t_freq) else ""
        return min_size 
                
            
            

def has_chrs(freq1, freq2):

    for key in freq2:
        if freq1[key] < freq2[key]:
            return False
    return True
