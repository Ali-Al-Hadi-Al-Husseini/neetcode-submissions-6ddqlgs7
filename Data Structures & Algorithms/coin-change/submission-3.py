class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def helper(amount):
            if amount < 0 :
                return float("inf"), False
            if amount == 0 :
                return 0 , True
            if amount in memo:
                return memo[amount], False

            min_coins = float("inf")
            is_finishable = False

            for  coin in coins:
                coins_count,is_finshed = helper(amount - coin)
                min_coins = min(min_coins, coins_count + 1)
                is_finishable |= is_finshed

            memo[amount] = min_coins
            return min_coins ,is_finishable

        coins_amount, is_solvable = helper(amount)
        return  coins_amount if is_solvable else -1 