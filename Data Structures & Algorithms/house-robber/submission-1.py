class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        return max(rob_helper(0,nums,memo), rob_helper(1,nums,memo))




    # idx = 0 memo = {} len(nums) = 4
def rob_helper(idx,nums,memo):
    if idx >= len(nums): return 0
    if idx in memo: return memo[idx]
    if idx == len(nums) -1 or idx ==len(nums)-2 : return nums[idx]

    # nums[idx] = 1 + max() nums[idx+2] = 3 
    memo[idx] = nums[idx] + max(rob_helper(idx+2,nums,memo), rob_helper(idx+3,nums,memo))

    return memo[idx] 
