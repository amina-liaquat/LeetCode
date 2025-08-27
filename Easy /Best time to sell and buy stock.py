class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        best_buy=prices[0]
        for i in range (1,len(prices)):
            best_buy=min(best_buy,prices[i])
            max_profit=max(max_profit,prices[i]-best_buy)
        return max_profit
       
        
