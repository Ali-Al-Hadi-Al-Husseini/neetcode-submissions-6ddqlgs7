class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ways = [0]

        def helper(idx,curr_sum):

            if curr_sum == target and idx == len(nums) - 1:
                ways[0] += 1
                return
            if idx >= len(nums) - 1:
                return 
            idx += 1
            helper(idx ,curr_sum + nums[idx])
            helper(idx ,curr_sum - nums[idx])
        helper(0,nums[0])
        helper(0,nums[0] * - 1)


        return ways[0]