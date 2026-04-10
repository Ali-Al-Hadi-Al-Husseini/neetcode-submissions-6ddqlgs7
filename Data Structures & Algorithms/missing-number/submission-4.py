class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        curr_sum = len(nums)

        for idx, num in enumerate(nums):
            curr_sum ^= num ^ idx

        return curr_sum 
    