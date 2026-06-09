class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        memo = {}
        def helper(arr):
            if len( arr) == 2 :
                return 0 
            if tuple(arr) in memo:
                return memo[tuple(arr)]
            max_val = float("-inf")

            for idx in range(1,len(arr) - 1):
                curr_val = arr[idx- 1]* arr[idx]*arr[idx +1]
                curr_val += helper(arr[:idx] + arr[idx + 1:])
                max_val = max(max_val,curr_val)

            memo[tuple(arr)] = max_val

            return max_val

        return helper(nums)
