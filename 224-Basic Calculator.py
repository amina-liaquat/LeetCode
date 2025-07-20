class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        res = 0
        num = 0
        sign = 1  # 1 means positive, -1 means negative

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == '+':
                res += sign * num
                num = 0
                sign = 1
            elif char == '-':
                res += sign * num
                num = 0
                sign = -1
            elif char == '(':
                # Push current result and sign to stack
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif char == ')':
                res += sign * num
                num = 0
                res *= stack.pop()  # Pop sign
                res += stack.pop()  # Pop previous result
            # Ignore spaces

        res += sign * num  # For the last number
        return res
