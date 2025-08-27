class Solution:
    def reverseWords(self, s: str) -> str:
      words = s.split()

      reversed_word = [] 

      for i in words:
        reverse_word = i[::-1]

        reversed_word.append(reverse_word)

      return " ".join(reversed_word)
        
