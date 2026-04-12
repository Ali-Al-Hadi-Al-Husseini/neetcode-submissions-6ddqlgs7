class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        def dfs():
            if len(curr) == len(nums):
                res.append(curr[:])
            if len(curr) >= len(nums):
                return

            curr_set = set(curr)
            for num in nums:
                if num in curr_set:
                    continue
                curr.append(num)
                dfs()
                curr.pop()
        dfs()
        return res
        






