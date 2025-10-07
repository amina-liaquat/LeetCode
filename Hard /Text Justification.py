class solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        n = len(words)

        while i < n:
            # Step 1: Determine how many words fit in the current line
            line_len = len(words[i])
            j = i + 1
            while j < n and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1

            # Step 2: Build the line from words[i:j]
            line_words = words[i:j]
            spaces_needed = maxWidth - sum(len(word) for word in line_words)

            # for word in line_words:
            #     len_word = len(word)


            # Case 1: Last line OR single word line → left justify
            if j == n or len(line_words) == 1:
                line = ' '.join(line_words)
                line += ' ' * (maxWidth - len(line))
            else:
                space_slots = len(line_words) - 1
                even_space = spaces_needed // space_slots
                extra_space = spaces_needed % space_slots

                line = ''
                for k in range(space_slots):
                    line += line_words[k]
                    line += ' ' * (even_space + (1 if k < extra_space else 0))
                line += line_words[-1]  # Last word (no extra space after)

            res.append(line)
            i = j  # Move to next group of words

        return res
        
