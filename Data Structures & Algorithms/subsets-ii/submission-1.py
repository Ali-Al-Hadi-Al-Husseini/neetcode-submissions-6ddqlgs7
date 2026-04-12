class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        sub_sets = []
        curr_set = []
        res_set =set()
        dfs(0,nums, curr_set, sub_sets, res_set)
        return sub_sets



def dfs(idx,nums, curr_set, sub_sets, res_set):
    if idx == len(nums):
        curr = curr_set[:]
        curr.sort()

        if tuple(curr) in res_set:
            return
        sub_sets.append(curr)
        res_set.add(tuple(curr))
        return

    curr_set.append(nums[idx])
    dfs(idx + 1, nums, curr_set, sub_sets, res_set)
    curr_set.pop()
    dfs(idx + 1, nums, curr_set, sub_sets, res_set )