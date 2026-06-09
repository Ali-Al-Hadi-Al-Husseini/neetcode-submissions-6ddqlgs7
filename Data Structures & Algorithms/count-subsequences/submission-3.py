class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}

        def helper(idx,length):
            if length == len(t):
                return 1 
            if (idx,length) in memo:
                return memo[(idx,length)]

            count = 0
            for i in range(idx+1,len(s)):
                if s[i] == t[length]:
                    count += helper(i,length+1)
            memo[(idx,length)] = count
            return count 

        return helper(-1,0)