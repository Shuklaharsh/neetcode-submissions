class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        countFreq = [0] * 26
        for i in range(0, len(s)):
            countFreq[ord(s[i]) - ord('a')] += 1
            countFreq[ord(t[i]) - ord('a')] -= 1

        for i in countFreq:
            if i>0:
                return False

        return True