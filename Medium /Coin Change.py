class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        bottomm up approach
        dp array  inf
        base case 0 
        fill array for each coin
        looping over coins
        min ()
        return combination
        
        """
        dp=[float("inf")] * (amount+1)
        dp[0]=0 # base case
        # filling and updating array
        for coin in coins:
            for x in range(coin,amount+1):
                dp[x]=min(dp[x],dp[x-coin]+1)

        return dp[amount] if dp[amount]!=float("inf") else -1

        
            # T :O(coin*amount)
            # S : O(amount)
