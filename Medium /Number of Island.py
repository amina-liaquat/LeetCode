class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        island = 0
        visit = set()
        def bfs(r,c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r, c))
            while q:
                row, col = q.popleft()
                directions = [[0, 1],[0, -1], [1, 0], [-1,0]]
                for dr, dc in directions:
                    r, c = row+dr, col+dc
                    if (r < rows and r >= 0 and
                        c < cols and c >= 0 and
                        (r, c) not in visit and grid[r][c] == '1'):
                        q.append((r, c))
                        visit.add((r, c))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] =='1' and (r, c) not in visit:
                    bfs(r, c)
                    island+=1
        return island
