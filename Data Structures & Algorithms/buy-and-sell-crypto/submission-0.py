class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit_yet = 0

        for idx,buy in enumerate(prices):
            for sell in prices[idx+1:]:
                max_profit_yet = max(max_profit_yet, sell - buy)

        return max_profit_yet