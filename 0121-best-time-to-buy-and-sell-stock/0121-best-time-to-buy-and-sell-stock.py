class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = prices[0]
        max_profit = 0
        for p in prices:
            # 
            if p < min_p:
                min_p = p
            # 
            curr_profit = p-min_p
            if curr_profit > max_profit:
                max_profit = curr_profit
        return max_profit
            
        