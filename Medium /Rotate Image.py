class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Transpose the matrix
        matrix[:] = list(map(list, zip(*matrix)))
        
        # Reverse each row
        for row in matrix:
            row.reverse()
