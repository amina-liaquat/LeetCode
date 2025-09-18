class Solution:
    def floodFill(self, image, sr, sc, newColor):
        # Get number of rows and columns
        rows, cols = len(image), len(image[0])
        
        # Save the original color of the starting pixel
        source = image[sr][sc]
        
        # If the new color is same as old color, nothing to do
        if source == newColor:
            return image

        # Define DFS function to fill pixels
        def dfs(r, c):
            # Stop if out of bounds OR pixel is not the source color
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != source:
                return

            # Fill the pixel with the new color
            image[r][c] = newColor

            # Visit all 4 neighbors (up, down, left, right)
            dfs(r - 1, c)  # top
            dfs(r + 1, c)  # bottom
            dfs(r, c - 1)  # left
            dfs(r, c + 1)  # right

        # Start DFS from the given starting pixel
        dfs(sr, sc)

        # Return the updated image
        return image
