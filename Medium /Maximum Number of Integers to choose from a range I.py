class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        count = 0
        computed_sum = 0
        for num in range(1, n + 1):
            if num not in banned and computed_sum + num <= maxSum:
                count += 1
                computed_sum += num
            elif computed_sum + num > maxSum:
                break
        return count
        
