class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sub_sets = []
        curr_set = []

        dfs(0,nums, curr_set, sub_sets)
        return sub_sets



def dfs(idx,nums, curr_set, sub_sets):
    if idx == len(nums):
        sub_sets.append(curr_set[:])
        return

    curr_set.append(nums[idx])
    dfs(idx + 1, nums, curr_set, sub_sets)
    curr_set.pop()
    dfs(idx + 1, nums, curr_set, sub_sets )