class Solution:
    def makeGood(self, s: str) -> str:
        stack =[]
        i = 0
        while i < len(s):
            if (
                stack # stack is not empty
                and stack[-1] != s[i] # both letters should not be same
                and stack[-1].lower() == s[i].lower() # their lower case must be same
            ):
                stack.pop()
            else: 
                stack.append(s[i])
            i += 1
        # [l,e,t]
        return "".join(stack)

# T.C = O(n)
# S.C = O(n)
        
