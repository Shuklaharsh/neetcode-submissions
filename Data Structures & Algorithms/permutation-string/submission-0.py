class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        countA = {}
        for i in s1:
            countA[i] = 1 + countA.get(i, 0)

        l, r = 0, 0
        countB = {}
        lenA = len(s1)
        while r < len(s2):
            while r - l + 1 <= lenA:
                countB[s2[r]] = 1 + countB.get(s2[r], 0)
                r += 1
            if countA == countB:
                return True
            
            countB[s2[l]] = countB.get(s2[l], 0) - 1
            if countB[s2[l]] == 0:   # 👈 remove when zero
                del countB[s2[l]]
            l += 1

        return False

            