class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0]== "0":
            return 0
        valid_pairs = set([str(x) for x in range(10,27)]) 
        dp = [1,1,0]
        
        for idx in range(2,len(s) + 1):   
            digit = s[idx -1]
            pair = s[idx- 2: idx]

            if digit != '0':
                dp[2] += dp[1]

            if pair in valid_pairs:
                dp[2] += dp[0]
                


            dp = [dp[1],dp[2],0]

        return dp[1] 



