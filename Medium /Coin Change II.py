class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def helper(i , remaining):
            if remaining == 0:
                return 1
            if (i, remaining) in memo:
                return memo[(i ,remaining)]
            if i == len(coins) or remaining < 0:
                return 0
            take = helper(i, remaining - coins[i])
            skip = helper(i + 1, remaining)
            memo[(i, remaining)] = take  + skip
            return memo[(i, remaining)]
        return helper(0,amount)
        
