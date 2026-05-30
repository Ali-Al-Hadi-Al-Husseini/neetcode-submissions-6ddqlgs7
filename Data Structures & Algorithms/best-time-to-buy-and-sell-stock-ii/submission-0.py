class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        

        for idx in range(1,len(prices)):
            if prices[idx] - prices[idx-1] > 0:
                total_profit += prices[idx] - prices[idx-1]
        return total_profit