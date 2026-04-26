class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        half_sum = sum(nums) / 2 
        
        def helper(idx,curr_set,curr_sum):
            if idx >= len(nums):
                return False
            if curr_sum == half_sum:
                return True

            return (helper(idx+1,curr_set + [nums[idx]], curr_sum + nums[idx]) or 
                    helper(idx+1,curr_set , curr_sum ))


        return helper(0,[],0)