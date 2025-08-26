class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix_sum = [0] * n
        suffix_sum[-1] = piles[-1]
        
        for i in range(n-2, -1, -1):
            suffix_sum[i] = suffix_sum[i+1] + piles[i]

        memo = {}

        def dp(i, M):
            if i + 2 * M >= n:
                return suffix_sum[i]
            
            if (i, M) in memo:
                return memo[(i, M)]

            max_stones = 0
            for X in range(1, 2 * M + 1):
                max_stones = max(max_stones, suffix_sum[i] - dp(i + X, max(M, X)))

            memo[(i, M)] = max_stones
            return max_stones

        return dp(0, 1)
        
