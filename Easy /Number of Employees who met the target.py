class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count=0
        for val in hours:
            if val >= target:
                count += 1
        return count
