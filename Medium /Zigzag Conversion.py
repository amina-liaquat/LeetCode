class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: if only one row, return the string itself
        if numRows == 1 or numRows >= len(s):
            return s

        # Create a list of strings for each row
        rows = [''] * numRows
        current_row = 0
        going_down = False

        # Iterate through each character
        for char in s:
            rows[current_row] += char
            # Change direction at the first or last row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            # Move up or down
            current_row += 1 if going_down else -1

        # Join all rows to form the final string
        return ''.join(rows)
