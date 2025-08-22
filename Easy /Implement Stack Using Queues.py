from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q2.append(x)  # Step 1: Push x into q2

        # Step 2: Push all elements of q1 to q2
        while self.q1:
            self.q2.append(self.q1.popleft())
        
        # Step 3: Swap the names of q1 and q2
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.popleft()  # Pop the front element of q1

    def top(self) -> int:
        return self.q1[0]  # Return the front element of q1

    def empty(self) -> bool:
        return not self.q1  # Return whether q1 is empty
