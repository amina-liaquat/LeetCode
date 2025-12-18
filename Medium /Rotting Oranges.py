from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        total_min = 0
        fresh = 0
        q = deque()
        total_mins = 0

        # loop on the grid
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        # BFS algo
        while q:
            if fresh == 0:
                break

            total_mins += 1

            # loop in 4 dimentions
            for _ in range(len(q)):
                i, j = q.popleft()
                for shift_r, shift_c in [(1,0), (0,1), (-1,0), (0,-1)]:
                    new_r, new_c = i + shift_r, j + shift_c
                    if 0 <= new_r < m and 0 <= new_c < n and grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2
                        fresh -= 1
                        q.append((new_r, new_c))

        if fresh != 0:
            return -1
        else: 
            return total_mins
