class Solution:
    def climbStairs(self, n: int) -> int:
        """
        (n-1) 
        two variables  one, two
        keep on updating then 
        return one
        """
        one=1
        two=1
        for i in range(n-1):
            temp=one
            one=one+two
            two=temp
        return one
