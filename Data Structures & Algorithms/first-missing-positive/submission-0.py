class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num_set = set(nums)
        min_pos_int = 1
        while min_pos_int in num_set:
            min_pos_int += 1
        return min_pos_int