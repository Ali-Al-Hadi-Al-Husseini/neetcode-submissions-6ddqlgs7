import sys
sys.setrecursionlimit(2000)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = sum(nums)
        curr_max = [curr_sum]
        interval = (0,len(nums))
        memo ={}
        helper(nums, curr_max,curr_sum,memo, interval)
        return curr_max[0]






def helper(nums, curr_max,curr_sum, memo,interval):
    if interval in memo: return memo[interval]
    if len(nums) == 1 : 
        curr_max[0] = max(curr_max[0],curr_sum)
        memo[interval] = curr_sum
        return 
    if len(nums) == 0 : return 


    helper(nums[1:],  curr_max , curr_sum - nums[0], memo,(interval[0] + 1,interval[1]))
    helper(nums[:-1], curr_max , curr_sum - nums[-1], memo,(interval[0],interval[1] - 1))
    helper(nums[1:-1],curr_max, curr_sum - nums[0] - nums[-1], memo,(interval[0] + 1,interval[1] - 1))

    curr_max[0] = max(curr_max[0],curr_sum)
    memo[interval] = curr_sum