class Solution:
    def fib(self, n: int) -> int:
        # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, and so on.
        # recursive approach
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)

        
        # res = {0: 0, 1: 1}
        # if n < 2:
        #     return res[n]
        # for i in range(2, n + 1):
        #     res[i] = res[i - 1] + res[i - 2]

        # return res[n]
        # more optimized approach
        # if n < 2:
        #     return n
        
        # prev1, prev2 = 0, 1  # Base cases: F(0) = 0, F(1) = 1
        # for _ in range(2, n + 1):
        #     current = prev1 + prev2
        #     prev1, prev2 = prev2, current  # Update the last two numbers
        
        # return prev2
        
