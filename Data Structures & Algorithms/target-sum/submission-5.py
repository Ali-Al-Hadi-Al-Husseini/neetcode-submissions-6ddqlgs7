class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def helper(idx, curr_sum):
            if idx == len(nums):
                return 1 if curr_sum == target else 0
            if (idx,curr_sum) in memo:
                return memo[(idx,curr_sum)]

            memo[(idx,curr_sum)] = helper(idx+ 1,curr_sum + nums[idx]) + helper(idx+ 1,curr_sum - nums[idx])

            return memo[(idx,curr_sum)]

        return helper(0,0)