class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if i == "D":
                stack.append(2*stack[-1])
            elif i == "+":
                stack.append(stack[-1] + stack[-2])
            elif i == "C":
                stack.pop()
            else:
                stack.append(int(i))
        return sum(stack)
        
