class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def get_max_seq_length(i,j):
            if i >=  len(text1) or j >= len(text2):
                return 0

            if (i,j) in memo:
                return memo[(i,j)]

            if text1[i] == text2[j]:
                memo[(i,j)] = 1 + get_max_seq_length(i +1, j +1)
                return memo[(i,j)]

            memo[(i+1,j)] = get_max_seq_length(i + 1,j)
            memo[(i,j + 1)] = get_max_seq_length(i, j +1)
            memo[(i,j)] = max(memo[(i,j + 1)], memo[(i+1,j)] )
            return memo[(i,j)] 

        
        return get_max_seq_length(0,0)