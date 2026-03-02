class Solution:
    def numTrees(self, n: int) -> int:
        # Create a DP array - gonna store number of unique BSTs for each count
        dp = [0] * (n + 1)
        
        dp[0] = 1   # Base case: empty tree counts as 1 way
        dp[1] = 1   # Base case: single node is also 1 way
        
        # Let's build up from 2 nodes to n nodes
        for nodes in range(2, n + 1):
            total_trees = 0  # renamed for clarity
            
            # Try each node as the root
            for root in range(1, nodes + 1):
                # Count left subtree possibilities
                left_count = dp[root - 1]
                
                # Count right subtree possibilities  
                right_count = dp[nodes - root]
                
                # Multiply them together (Cartesian product basically)
                total_trees += left_count * right_count
                
            dp[nodes] = total_trees
        
        # Return the result for n nodes
        return dp[n]
