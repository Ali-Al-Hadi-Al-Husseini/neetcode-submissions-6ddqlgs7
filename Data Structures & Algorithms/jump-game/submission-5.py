

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        destination = len(nums) - 1 
        idx = destination - 1 

        while idx >= 0 :
            if nums[idx] + idx >= destination:
                destination = idx
            

            idx -= 1 

        return destination == 0 