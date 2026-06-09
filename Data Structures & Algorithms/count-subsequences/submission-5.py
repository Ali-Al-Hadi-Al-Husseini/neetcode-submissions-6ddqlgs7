class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}

        def helper(i,j):
            if i == len(t):
                return 1
            if j == len(s):
                return 0
            if (i,j) in memo:
                return memo[(i,j)]

            count = helper(i,j+1)

            if t[i] == s[j]:
                count += helper(i+1,j+1)
            memo[(i,j)] = count
            return count 

        return helper(0,0)