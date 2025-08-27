class Solution(object):
    def longestWord(self, words):
        words.sort()

        words_set = set()
        words_set.add("")
        longest_word = ""

        for word in words:
            if  word[0:-1] in words_set:
                words_set.add(word)

                if len(word) > len(longest_word):
                    longest_word = word
        
        return longest_word

# time complexity: O(n log n)
# space complexity: O(n)
