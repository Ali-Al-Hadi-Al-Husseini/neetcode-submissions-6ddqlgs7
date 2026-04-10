class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        return min(helper(cost,0,memo),helper(cost,1,memo))


def helper(cost,idx,memo):
    if idx >= len(cost): return 0
    if idx in memo: return memo[idx]

    memo[idx] = cost[idx] + min(helper(cost,idx+1,memo) ,helper(cost,idx+2,memo))

    return memo[idx]