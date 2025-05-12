class Solution:
    def uniqueMorseRepresentations(self, words):
        # Morse codes for letters a to z
        morse_codes = [
            ".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
            "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
            "..-","...-",".--","-..-","-.--","--.."
        ]
        
        # Set to store unique Morse transformations
        transformations = set()
        
        # For each word in the input list
        for word in words:
            morse_word = ""
            for char in word:
                # Convert character to index (ord('a') = 97)
                index = ord(char) - ord('a')
                morse_word += morse_codes[index]
            
            # Add the transformed Morse word to the set
            transformations.add(morse_word)
        
        # Return number of unique transformations
        return len(transformations)
