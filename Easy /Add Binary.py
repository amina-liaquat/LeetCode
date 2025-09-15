class Solution:
    def addBinary(self, a: str, b: str) -> str:

        # Step 1: Convert binary string 'a' into decimal (base 10) using int() with base=2
        decimal_a = int(a, 2)   # Example: int("11", 2) = 3

        # Step 2: Convert binary string 'b' into decimal (base 10)
        decimal_b = int(b, 2)   # Example: int("1", 2) = 1

        # Step 3: Add the two decimal values
        total = decimal_a + decimal_b   # Example: 3 + 1 = 4

        # Step 4: Convert the result back into binary using bin()
        # bin(4) returns "0b100", so we remove "0b" by slicing [2:]
        binary_sum = bin(total)[2:]

        # Step 5: Return the final binary string
        return binary_sum
