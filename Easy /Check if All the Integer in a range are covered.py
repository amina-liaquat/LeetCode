class Solution:
    def isCovered(self, ranges, left, right):
        covered = [0] * 52

        for start, end in ranges:
            for i in range(start, end + 1):
                covered[i] = 1

        for i in range(left, right + 1):
            if covered[i] == 0:
                return False

        return True
