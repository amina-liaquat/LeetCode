class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()      # bring duplicates together
        result = []

        def backtrack(index, current):
            # every path is a valid subset
            result.append(current[:])

            for i in range(index, len(nums)):
                # skip duplicate numbers
                if i > index and nums[i] == nums[i - 1]:
                    continue

                current.append(nums[i])      # choose
                backtrack(i + 1, current)    # explore
                current.pop()                # undo choice

        backtrack(0, [])
        return result
