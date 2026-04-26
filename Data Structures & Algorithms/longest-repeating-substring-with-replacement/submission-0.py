class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        countFreq = {}
        l = 0
        res = 0
        maxf= 0
        for r in range(len(s)):
            countFreq[s[r]] = 1 + countFreq.get(s[r], 0)
            maxf = max(maxf, countFreq[s[r]])
            while (r - l + 1) - maxf > k:
                countFreq[s[l]] -= 1
                l += 1
            
            res = max(r - l + 1, res)

        return res