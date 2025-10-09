class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = Counter(s)
        seen = set()
        stack = []

        for i in s:
            counter[i] -= 1
            if i in seen:
                continue

            while stack and i < stack[-1] and counter[stack[-1]] > 0:
                removed = stack.pop()
                seen.remove(removed)
            stack.append(i)
            seen.add(i)

        return ''.join(stack)
