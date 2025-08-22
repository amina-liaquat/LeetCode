class Solution:
   def triangleType(self, nums: List[int]) -> str:
      a=nums[0]
      b=nums[1]
      c=nums[2]
      if a + b > c and b + c > a and c + a > b:
            if a == b == c:
                return "equilateral"
            elif a == b or b == c or a == c:
                return "isosceles"
            else:
                return "scalene"
      return "none"

