class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        candidates.sort()
        def DFS(idx,total): # curr = [2,2,4]
            if total == target: # idx = 3, total = 8
                res.append(curr[:])
                 
            if idx >= len(candidates) or total >= target:
                return

            curr.append(candidates[idx])
            DFS(idx + 1 , total + candidates[idx])
            curr.pop()
            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx + 1]:
                idx+= 1
            DFS(idx + 1, total)

        DFS(0,0)
        return res