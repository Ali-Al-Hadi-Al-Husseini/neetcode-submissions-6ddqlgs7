class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        curr_sum = 0
        should_be = 0

        for n in range(len(nums)+ 1):
            should_be ^= n

        for num in nums:
            curr_sum ^= num

        return curr_sum ^ should_be 

    