class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reversed_num = 0
        original_num = x
        while x != 0:
            pop = x % 10
            x //= 10
            reversed_num = reversed_num * 10 + pop
        return original_num == reversed_num

        
