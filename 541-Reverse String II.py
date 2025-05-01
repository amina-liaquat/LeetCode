class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)    #O(n)
        for i in range(0, len(s), 2*k):   #O(n/2k)
            s[i:i+k] = reversed(s[i:i+k])   #O(k)

        return "".join(s)
  

  #Time Complexity = O(n)
  #Space Complexity = O(n)
