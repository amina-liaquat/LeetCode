class solution:
     def backspaceCompare(self, s: str, t: str) -> bool:
         stack_s, stack_t=[],[] #(m+n)
 
         for i in s:
             if(i=='#'):
                 if stack_s:
                     stack_s.pop()
             else:
                 stack_s.append(i)
 
         for j in t:
             if(j=='#'):
                 if stack_t:
                     stack_t.pop()
             else:
                 stack_t.append(j)
         
         if stack_s == stack_t:
             return True
         
         else:
             return False
        
