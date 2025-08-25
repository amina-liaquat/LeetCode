class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        # Initialize the left pointer
        left = 0

        # Iterate over the array with the right pointer
        for right in range(1, len(nums)):
            # If the current number is different from the one at the left pointer
            if nums[right] != nums[left]:
                left += 1
                nums[left] = nums[right]

        # The new length of the array with unique elements is left + 1
        return left + 1

