class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        memo ={}
        n = len(grid)
        m = len(grid[0])
        if n == 1 and m == 1 and grid[n - 1][m - 1] == 1:
            return 0
        if grid[n - 1][m - 1] == 1:
            return  0
        def helper(i, j):
            if (i , j) in memo:
                return memo[(i , j)]
            if i == n - 1 and j == m - 1:
                return 1
            if i >= n or j >= m:
                return 0
            if grid[i][j] == 1:
                return 0
            right = helper(i , j + 1)
            down  = helper(i + 1, j)
            memo[(i, j)] = right + down
            return memo[(i, j)]
        return helper(0 , 0)
