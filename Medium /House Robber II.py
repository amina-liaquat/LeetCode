class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # Handle edge cases
        if n == 0: return 0
        if n == 1: return nums[0]
        
        # Scenario 1: Rob from first house to second-to-last (skip last)
        # Scenario 2: Rob from second house to last (skip first)
        return max(self.linear_rob(nums[1:]), self.linear_rob(nums[:-1]))

    def linear_rob(self, houses):
        """Standard House Robber I solution (i+1, i+2 logic)"""
        prev2 = 0 # dp[i-2]
        prev1 = 0 # dp[i-1]
        
        for money in houses:
            # new_max = max(rob_current + dp[i-2], skip_current + dp[i-1])
            new_max = max(prev2 + money, prev1)
            prev2 = prev1
            prev1 = new_max
            
        return prev1
        
