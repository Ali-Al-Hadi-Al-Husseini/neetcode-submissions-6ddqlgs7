class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        return helper(0,0,nums)




def helper(idx, total, nums):
    if idx== len(nums): return total

    return helper(idx+ 1 ,total ^nums[idx],nums) + helper(idx + 1 ,total,nums)