class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {0:0,1:1,2:1,3:2}
        return tribonacci_helper(n,memo)



def tribonacci_helper(n,memo):
    if n <= 0 :return 0
    if n in memo: return memo[n]

    memo[n] = tribonacci_helper(n-1,memo) +tribonacci_helper(n-2,memo)+ tribonacci_helper(n-3,memo)
    return memo[n]