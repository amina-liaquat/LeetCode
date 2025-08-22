class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            # print(s[i])
            if s[i] == '*':
                stack.pop() # removing last element / character
            else:
                stack.append(s[i])
        # return stack
        # return "".join(stack) # converts the elements in list into string
        a = ""
        for i in range(len(stack)):
            a = stack.pop() + a # eocel - lecoe
            a[::-1] # to reverse the string
        return a 
