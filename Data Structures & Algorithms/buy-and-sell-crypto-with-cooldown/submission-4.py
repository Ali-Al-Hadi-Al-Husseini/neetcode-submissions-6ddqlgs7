class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        usage = defaultdict(int)
        def get_max_profit(idx, bought):
            if idx >= len(prices):
                return 0

            if (idx,bought)  in memo:
                val =  memo[((idx,bought))]
                # each val is only accsed one time after assiment 
                del memo[((idx,bought))]
                return val


            holding_profit = get_max_profit(idx+1,bought)
            if not bought:
                buying_profit = get_max_profit(idx+1,True) - prices[idx]
                memo[(idx,bought)] = max(holding_profit, buying_profit)
            else:
                selling_profit = get_max_profit(idx+2,False) + prices[idx]
                memo[(idx,bought)] = max(holding_profit,selling_profit)


            return memo[(idx,bought)]
          
        ret =  get_max_profit(0,False)
        return ret