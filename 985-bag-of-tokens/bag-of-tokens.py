class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        low = 0
        score = 0
        high = len(tokens)-1
        while low <= high:
            if power >= tokens[low]:
                score += 1
                power -= tokens[low]
                low += 1
            elif score > 0 and low < high:
                score -= 1
                power += tokens[high]
                high -= 1
            else:
                return score
        return score
        