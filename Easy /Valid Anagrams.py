class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       a=sorted(s)
       b=sorted(t)
       return a==b
