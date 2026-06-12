class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        bin_count = {}
        memo = {}

        def helper (idx,m,n):
            if idx >= len(strs) or ( m==0 and  n== 0 ):
                return 0
            if (idx,m,n) in memo:
                return memo[(idx,m,n)]
            
            max_size = 0
            zeros,ones = get_bin_count(strs[idx]) if strs[idx] not in   bin_count else bin_count[strs[idx]]
            if m-zeros >= 0 and n - ones >= 0 :
                max_size =  helper(idx+1,m-zeros,n-ones) + 1

            max_size = max(max_size,helper(idx+1,m,n))
            memo[(idx,m,n)] = max_size

            return max_size

        return helper(0,m,n) 



def get_bin_count(string):
    zeros = 0
    ones = 0


    for _bit in string:
        if _bit == "1":
            ones += 1
        elif _bit == "0":
            zeros += 1

    return zeros,ones