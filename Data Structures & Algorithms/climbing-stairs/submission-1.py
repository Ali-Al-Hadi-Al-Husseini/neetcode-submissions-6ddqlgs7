class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {2:2,1:1}
        return climb_stairs_helper(n,memo)
        

def climb_stairs_helper(n ,memo):
    if n <=0: return 0
    if n in memo: return memo[n]
    memo[n] = climb_stairs_helper(n-1,memo)+ climb_stairs_helper(n-2,memo)
    return memo[n]



"""
 n = 2 
        1 -> 1
        2 

n = 3   
        1 -> 1 -> 1 
        1 -> 2
        2 -> 1  

"""