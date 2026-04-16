import sys

# sys.rec
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        return dfs(0,nums)

def dfs(idx,  nums):
    if idx >= len(nums) - 1: return True
    
    
    for i in reversed(range(1,nums[idx] + 1 )):

        if dfs(idx + i, nums):
            return True


    return False