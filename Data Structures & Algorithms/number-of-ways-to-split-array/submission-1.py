class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        num_sum = sum(nums)
        curr_sum = 0
        res = 0

        for i in range(len(nums) - 1):
            curr_sum += nums[i]
            num_sum -= nums[i]

            if curr_sum  >= num_sum:
                res += 1 

        return res 
