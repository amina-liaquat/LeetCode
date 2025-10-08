class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)        # number of rows
        n = len(grid[0])     # number of columns
        result = []          # to store where each ball ends up

        for col in range(n):     # drop one ball from each column
            curr_col = col       # start column of the ball
            for row in range(m): # go through each row
                dir = grid[row][curr_col]            # direction in current cell
                next_col = curr_col + dir            # where the ball wants to go

                # if the ball goes out of bounds or hits a V shape trap
                if next_col < 0 or next_col >= n or grid[row][next_col] != dir:
                    curr_col = -1   # ball is stuck
                    break
                curr_col = next_col  # move ball to the next column
            result.append(curr_col) # store the result

        return result
      
