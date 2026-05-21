class Solution:
    def jump(self, nums: List[int]) -> bool:
        memo = {}
        def dfs(idx):
            if idx >= len(nums) - 1: return 0
            if nums[idx] == 0 :
                return 1
            if idx in memo: return memo[idx]
            

            paths = []
            for i in reversed(range(1,nums[idx] + 1 )):
                paths.append(dfs(idx + i))
                
            memo[idx] =  (min(paths) if len(paths) > 0 else 0 ) + 1 
            return memo[idx]
        return dfs(0)

