class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        most_one = 0
        curr_ones = 0
        idx = 0

        while idx < len(nums):
            
            while idx < len(nums) and nums[idx] == 1 :
                curr_ones +=1 
                idx +=1 
            most_one = max(most_one, curr_ones)
            curr_ones = 0

            idx += 1 


        return most_one