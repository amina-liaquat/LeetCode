class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",
                 ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
                 "...","-","..-","...-",".--","-..-","-.--","--.."]
        
        transformations = set()  # To store unique Morse strings
        
        for word in words:
            transformation = ''
            for char in word:
                transformation += morse[ord(char) - ord('a')]
            transformations.add(transformation)
        
        return len(transformations)
