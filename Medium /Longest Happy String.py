class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # Max-heap of available characters and their counts
        heap = []
        if a > 0:
            heapq.heappush(heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(heap, (-c, 'c'))

        result = []
        
        # While there are still characters left to append
        while heap:
            # Get the character with the most remaining occurrences
            count1, char1 = heapq.heappop(heap)
            
            # Check if appending this character would violate the rule
            if len(result) >= 2 and result[-1] == result[-2] == char1:
                if not heap:
                    break  # No other characters to use, stop
                # Otherwise, take the next most frequent character
                count2, char2 = heapq.heappop(heap)
                result.append(char2)
                if count2 + 1 < 0:
                    heapq.heappush(heap, (count2 + 1, char2))  # Push back if any left
                # Push the first character back into the heap
                heapq.heappush(heap, (count1, char1))
            else:
                # Safe to append char1
                result.append(char1)
                if count1 + 1 < 0:
                    heapq.heappush(heap, (count1 + 1, char1))  # Push back if any left
        
        return ''.join(result)
        
