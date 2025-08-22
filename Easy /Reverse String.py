class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) -1
        for i in range (len(s)//2):
          if l == r:
              break
          s[l] , s[r] = s [r],s[l]
          l += 1
          r -= 1
        return s
        # return s.reserve()
