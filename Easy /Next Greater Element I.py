class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        next_greater_nums = {}
        stack = []

        for i in nums2:
            while stack and i > stack[-1]:
                smaller_val = stack.pop()
                next_greater_nums[smaller_val] = i
            stack.append(i)

        while stack:
            next_greater_nums[stack.pop()] = -1

        res =[]
        for i in nums1:
            res.append(next_greater_nums[i])

        return res
