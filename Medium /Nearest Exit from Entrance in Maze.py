from collections import deque
from typing import List

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        q = deque()
        q.append((entrance[0], entrance[1], 0))

        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        rows, cols = len(maze), len(maze[0])

        # mark entrance as visited
        maze[entrance[0]][entrance[1]] = '+'

        while q:
            row, col, steps = q.popleft()

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == '.':
                    if nr == 0 or nr == rows-1 or nc == 0 or nc == cols-1:
                        return steps + 1

                    maze[nr][nc] = '+'
                    q.append((nr, nc, steps + 1))

        return -1
