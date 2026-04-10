class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        concatention = nums[:]
        concatention.extend(nums)
        return concatention
        