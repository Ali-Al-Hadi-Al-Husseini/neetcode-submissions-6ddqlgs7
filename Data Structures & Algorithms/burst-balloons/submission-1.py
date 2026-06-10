class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        memo = {}


        def helper(l,r) -> int:
            if l > r:
                return 0
            if (l,r) in memo:
                return memo[(l,r)]


            memo[(l,r)] = 0
            for i in range(l,r+1):
                curr = nums[l-1] *nums[i] *nums [r+1]
                curr += helper(i+1,r) + helper(l,i - 1)
                memo[(l,r)] = max(curr, memo[(l,r)] )

            return  memo[(l,r)] 


        return helper(1,len(nums) -2 )
            