class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        curr_sum = 0

        for idx, num in enumerate(nums):
            curr_sum ^= num
            curr_sum ^= idx


        return curr_sum ^ (idx + 1 ) 
    