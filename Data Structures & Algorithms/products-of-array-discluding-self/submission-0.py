class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1 for _ in nums ]
        accumaltion = 1
        rev_accum = 1 
        for idx in range(len(nums)) :
            output[idx] *= accumaltion
            output[len(output) - idx - 1 ] *= rev_accum
            accumaltion *= nums[idx]
            rev_accum *= nums[len(output) - idx - 1]

        return output 
        