class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []


        def dfs(idx, curr, total):
            if total == target:
                result.append(curr[:])
                
            if idx >= len(nums) or total >= target:
                return
            
            curr.append(nums[idx])
            dfs(idx,curr, total + nums[idx])
            curr.pop()
            dfs(idx + 1, curr,total)

        dfs(0,[], 0)
        return result


        
