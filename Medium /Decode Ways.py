class Solution:
    def numDecodings(self, s: str) -> int:
        # If the string starts with '0', no valid decodings exist
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        dp = [0] * (n + 1)
        
        dp[0] = 1  # Empty string → 1 way
        dp[1] = 1  # First character (not '0') → 1 way
        
        for i in range(2, n + 1):
            one_digit = int(s[i-1:i])      # current single digit
            two_digits = int(s[i-2:i])     # current two digits
            
            # If single digit is valid (1–9)
            if 1 <= one_digit <= 9:
                dp[i] += dp[i - 1]
            
            # If two digits form a valid code (10–26)
            if 10 <= two_digits <= 26:
                dp[i] += dp[i - 2]
        
        return dp[n]
