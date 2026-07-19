class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False 

        memo = {}

        def helper(i,j,k):
            if k == len(s3):
                return i == len(s1) and j == len(s2)
            if (i,j) in memo:
                return memo[(i,j)]

            result = False
            if i < len(s1) and s1[i] == s3[k]:
                result |= helper(i+1,j,k+1)
            if j < len(s2) and s2[j] == s3[k]:
                result |= helper(i,j+1,k+1)

            memo[(i,j)] = result
            return result

        return helper(0,0,0)
