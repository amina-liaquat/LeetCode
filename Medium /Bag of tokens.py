class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort() # O(logn)

        l, r = 0, len(tokens)-1
        score, result = 0, 0

        while l <= r:
            # face up
            if power >= tokens[l]:
                power -= tokens[l] # 100 - 50 = 50
                score += 1
                l += 1
                result = max(result, score)
            # face down
            elif score > 0:
                power += tokens[r]
                score -= 1
                r -= 1
            else:
                break
        return result

# time: O(nlogn)
# space: O(1)
        
