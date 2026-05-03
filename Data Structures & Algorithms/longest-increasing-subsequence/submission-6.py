class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def find_longrst_sub_sequence(idx):
            if idx in memo:
                return memo[idx]
                
            curr_max = 1
            for j in range(idx+1,len(nums)):
                if nums[j] <= nums[idx]:
                    continue    
                
                curr_max = max(find_longrst_sub_sequence(j) +1 ,  1,curr_max)
        
            memo[idx] = curr_max
            return curr_max

        return max( find_longrst_sub_sequence(idx) for idx in range(len(nums)))
    