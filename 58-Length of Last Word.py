class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = ''
        words = []
        for i in range(len(s)):
            if s[i] != ' ':
                word += s[i]
            elif word:
                words.append(word)
                word = ''
        if word:
            words.append(word)

        return len(words[-1]) if words else 0
