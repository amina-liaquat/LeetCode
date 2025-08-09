class Solution:
    def minimumSteps(self, s: str) -> int:
        block_ball_count  = 0
        total_swaps =  0
        for i in range(len(s)):
            if s[i] == "1":
                block_ball_count += 1
            else:
                total_swaps +=  block_ball_count
        return total_swaps
