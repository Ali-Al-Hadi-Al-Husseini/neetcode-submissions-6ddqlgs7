class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}

        def helper(curr_sum):
            if curr_sum == target:
                return 1
            if curr_sum > target:
                return 0
            if curr_sum in memo:
                return memo[curr_sum]

            count = 0
            for num in nums:
                count += helper(curr_sum + num)
            memo[curr_sum] = count
            return count
        return helper(0)