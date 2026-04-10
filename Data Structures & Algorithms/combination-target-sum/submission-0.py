class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = set()


        def dfs(curr_sum):
            sum_curr = sum(curr_sum)
            if sum_curr == target:
                curr_sum.sort()
                result.add(tuple(curr_sum))
            if sum_curr >= target:
                return 
            
            for num in nums :
                dfs(curr_sum + [num])

        dfs([])
        return [list(tup) for tup in result ]



        
