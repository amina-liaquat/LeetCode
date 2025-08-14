class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        # Iterate through each sentence in the list
        # Convert sentence into list
        # find the maximum words in a sentence
        # Return maximum words

        print("max-->", max(2, 4))

        max_count = 0

        for i in range(len(sentences)):
            print(i)
            print(sentences[i])

            words = sentences[i].split(" ")
            # print("words-->", words)

            max_count = max(max_count, len(words))

        return max_count
