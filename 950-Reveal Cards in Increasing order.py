class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n = len(deck)
        result = [0] * n
        indices = deque(range(n)) # deque([0, 1, 2, 3, 4, 5, 6])
        
        for card in deck:
            index = indices.popleft()
            result[index] = card       
            if indices:              
                indices.append(indices.popleft())  

        return result
