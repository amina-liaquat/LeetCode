class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldier_count = []
        
        # Calculate the number of soldiers in each row
        for i, row in enumerate(mat):
            count = sum(row)  # Count of soldiers (1s) in the row
            soldier_count.append((count, i))  # Store (number of soldiers, row index)
        
        # Sort the list by number of soldiers, then by row index
        soldier_count.sort()
        
        # Extract the first k row indices from the sorted list
        return [i for _, i in soldier_count[:k]]   
        
