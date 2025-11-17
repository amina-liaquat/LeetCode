class Solution:
  def maxProduct(self, nums: List[int]) -> int:
    return self.maxProductRecursive(nums, 0, len(nums) - 1)

  def maxProductRecursive(self, nums: List[int], start: int, end: int) -> int:
    if start > end:
      return float('-inf')

    if start == end:
      return nums[start]

    max_prod = float('-inf')
    segment_start = start
    found_zero = False

    for i in range(start, end + 1):
      if nums[i] == 0:
        found_zero = True
        max_prod = max(max_prod, self.maxProductRecursive(nums, segment_start, i - 1))
        segment_start = i + 1

    # Process the final segment after the last zero
    max_prod = max(max_prod, self.maxProductInZeroFreeSegment(nums, segment_start, end))

    return max(0, max_prod) if found_zero else max_prod

  def maxProductInZeroFreeSegment(self, nums: List[int], start: int, end: int) -> int:
    if start > end:
      return float('-inf')

    total_product = 1
    negative_count = 0
    first_negative = -1
    last_negative = -1

    # Calculate total product and track first/last negative indices
    for i in range(start, end + 1):
      total_product *= nums[i]
      if nums[i] < 0:
        negative_count += 1
        if first_negative == -1:
          first_negative = i
        last_negative = i

    if negative_count % 2 == 0:
      return total_product

    # If odd number of negatives, exclude left or right side
    left_product = 1
    max_left = float('-inf')
    for i in range(first_negative + 1, end + 1):
      left_product *= nums[i]
      max_left = max(max_left, left_product)

    right_product = 1
    max_right = float('-inf')
    for i in range(last_negative - 1, start - 1, -1):
      right_product *= nums[i]
      max_right = max(max_right, right_product)

    return max(max_left, max_right)
