class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []  # Stack to keep track of surviving asteroids
        
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0: 
                
    #stack : Check if there are asteroids in the stack to collide with.
    # a < 0): The current asteroid is moving to the left.
    #stack[-1] > 0: The top asteroid in the stack is moving to the right.
    
                diff = a + stack[-1]
                if diff < 0:  # Current asteroid is stronger
                    stack.pop()  # Remove the top asteroid from the stack
                elif diff > 0:  # Stack's top asteroid is stronger
                    a = 0  # Current asteroid is destroyed
                else:  # Both are of equal size
                    a = 0  # Both are destroyed
                    stack.pop()
            
            if a:  # If the current asteroid survives, add it to the stack
                stack.append(a)
        
        return stack
