class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def helper(i,j,):
            if i == len(word1):
                return  len(word2) - j
            if j == len(word2):
                return len(word1) - i
            if (i,j) in memo:
                return memo[(i,j)]

            res = float("inf")
            if word1[i] == word2[j]:
                res = helper(i +1,j +1)
            else:
                res = min(
                    helper(i+1,j,),# delete
                    helper(i,j+1,), # insert
                    helper(i+1,j+1,) # replace
                ) + 1
            memo[(i,j)] = res
            return res

        return helper(0,0)