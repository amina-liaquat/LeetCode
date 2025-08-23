class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        
        def Checking(row, col, rule):
            array = []

            if col > 0:
                array.append(board[row][col-1])
            
            if col < cols-1:
                array.append(board[row][col+1])

            if row > 0:
               array.append(board[row-1][col])

            if row < rows-1:
                array.append(board[row+1][col])
            
            if row > 0 and col > 0:
                array.append(board[row-1][col-1])
            
            if row < rows-1 and col < cols-1:
               array.append(board[row+1][col+1])

            if row > 0 and col < cols-1:
                array.append(board[row-1][col+1])
            
            if row < rows-1 and col > 0:
                array.append(board[row+1][col-1])
            
            if rule == 1:
                return array.count(1) + array.count(2) < 2
            if rule == 2:
                return (array.count(1) + array.count(2)) in (2, 3)
            if rule == 3:
                return array.count(1) + array.count(2) > 3
            if rule == 4:
                return array.count(1) + array.count(2) == 3
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 1 and Checking(row, col, 1):
                    board[row][col] = 2
                
                if board[row][col] == 1 and Checking(row, col, 2):
                    board[row][col] = 1
                
                if board[row][col] == 1 and Checking(row, col, 3):
                    board[row][col] = 2
                
                if board[row][col] == 0 and Checking(row, col, 4):
                    board[row][col] = 3
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 2:
                    board[row][col] = 0
                if board[row][col] == 3:
                    board[row][col] = 1
        
