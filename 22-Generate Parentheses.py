class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open paranthesis if open<n
        # ony add a closing paranthesis if closed < open
        # valid if opn==closed==n

        stack = []  # to hold our paranthesis

        res = []   # list of valid paranthesis combinations

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return 
                
            if openN < n:
                stack.append("(")
                backtrack(openN+1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtrack(openN,closedN+1)
                stack.pop()

        backtrack(0,0)
        return res
        
