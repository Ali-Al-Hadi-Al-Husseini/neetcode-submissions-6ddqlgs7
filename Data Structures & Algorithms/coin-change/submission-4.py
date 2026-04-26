class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def helper(curr_amount):
            if curr_amount > amount :
                return float("inf"), False
            if amount == curr_amount :
                return 0 , True
            if curr_amount in memo:
                return memo[curr_amount], False

            min_coins = float("inf")
            is_finishable = False

            for  coin in coins:
                coins_count,is_finshed = helper(curr_amount + coin)
                min_coins = min(min_coins, coins_count + 1)
                is_finishable |= is_finshed

            memo[curr_amount] = min_coins
            return min_coins ,is_finishable

        coins_amount, is_solvable = helper(0)
        return  coins_amount if is_solvable else -1 