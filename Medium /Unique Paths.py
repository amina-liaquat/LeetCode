class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 2d
        record = [[0] * n for _ in range(m)]

        def rec(r, c):
            # base
            if r == m-1 and c == n-1:
                return 1
            if r<0 or r>=m or c < 0 or c>= n:
                return 0
            
            if record[r][c] != 0:
                return record[r][c]

            # explore the possible ways
            record[r][c] = rec(r+1, c) + rec(r, c+1)
            return record[r][c]

        return rec(0, 0) # record[0][0]
