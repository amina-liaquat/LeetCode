class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        count = [0, 0]  # count[0] = circular lovers, count[1] = square lovers

        # Count how many students prefer each type of sandwich
        for student in students:
            count[student] += 1

            # count [2, 2 ]

        # Go through the sandwich stack
        for sandwich in sandwiches:
            # If no student wants this type, break out
            if count[sandwich] == 0:
                break
            count[sandwich] -= 1  # One student eats the sandwich

        # Remaining students couldn't eat
        return sum(count)
        
