class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = set(jewels)  # Correct variable name and consistent usage.
        count = 0

        for stone in stones:  # Proper indentation of the loop.
            if stone in jewels_set:
                count += 1

        return count  # Proper indentation of the return statement.
