class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # If k >= length of number, removing all digits means result is "0"
        if k >= len(num):
            return "0"
        
        stack = []  # Monotonic increasing stack

        for c in num:
            # Remove previous larger digits to make number smaller
            while k > 0 and stack and stack[-1] > c:
                stack.pop()
                k -= 1
            stack.append(c)

        # If we still have k > 0, remove from the end
        while k > 0:
            stack.pop()
            k -= 1

        # Join stack into a string
        result = ''.join(stack)
        # Remove leading zeros
        result = result.lstrip('0')

        # If result is empty, return "0"
        return result if result else '0'
        
