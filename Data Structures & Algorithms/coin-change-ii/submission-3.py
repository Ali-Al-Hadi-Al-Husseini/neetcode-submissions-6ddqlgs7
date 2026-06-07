class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        coins.sort()
        
        def helper(curr_amount,idx):
            if curr_amount > amount or idx >= len(coins)  :
                return 0 
            if curr_amount == amount:
                return 1
            if (curr_amount,idx) in memo:
                return memo[(curr_amount,idx)]
            ways = helper(curr_amount,idx+1)
            ways += helper(curr_amount + coins[idx],idx)
            memo[(curr_amount,idx)] = ways

            return ways

        return helper(0,0) 