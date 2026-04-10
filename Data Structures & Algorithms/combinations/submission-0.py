class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        curr = []

        def dfs(curr_num):
            if len(curr) == k :
                res.append(curr[:])
                return 
            if curr_num > n:
                return 
            
            curr.append(curr_num)
            dfs(curr_num + 1  )
            curr.pop()
            dfs(curr_num + 1)
                
            
            
        dfs(1)
        return res



def dfs(curr,nums,k,res):
    if len(curr)== k:
        res.append(curr)
    if len(curr) >= k:
        return 

    curr_set = set(curr)
    for num in nums:
        if num in curr_set:
            continue
        dfs(curr + [num], nums,k,res)
    