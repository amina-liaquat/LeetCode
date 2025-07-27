class Solution:
    def decodeString(self, s: str) -> str:
     
     stack = []
     for i in range(len(s)):
        if s[i] != ']':
            stack.append(s[i])
        else:
            a = ""
            while stack[-1] != '[':
                a = stack.pop() + a
            stack.pop()  

           
            multiplier = ""
            while stack and stack[-1].isdigit():
                multiplier = stack.pop() + multiplier

           
            multiplier = int(multiplier) if multiplier else 1

    
            stack.append(a * multiplier)

     return "".join(stack)
