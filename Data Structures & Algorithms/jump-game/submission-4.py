

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        return dfs(0,nums)

def dfs(idx,  nums):
    if idx >= len(nums) - 1: return True
    if nums[idx] == -1 : return False
    for i in reversed(range(1,nums[idx] + 1 )):
        if dfs(idx + i, nums):
            return True

    nums[idx] = -1
    return False