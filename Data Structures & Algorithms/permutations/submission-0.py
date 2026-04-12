class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        dfs([],nums,res)
        return res
        






def dfs(curr, nums, res):
    if len(curr) == len(nums):
        res.append(curr)
    if len(curr) >= len(nums):
        return

    curr_set = set(curr)
    for num in nums:
        if num in curr_set:
            continue
        dfs(curr + [num],nums,res )