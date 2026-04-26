class Solution:

    def matchCount(self, countT, countS):
        for k, v in countT.items():
            if k not in countS:
                return False
            
            if countS[k] < v:
                return False

        return True

    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        countT = {}
        countS = {}
        for i in t:
            countT[i] = 1 + countT.get(i, 0)
        
        l, r, res = 0, 0, ""
        while r < len(s) and s[r] not in countT:
            r += 1
            l += 1
        while r < len(s):
            if s[r] in countT:
                countS[s[r]] = 1 + countS.get(s[r], 0)

            if self.matchCount(countT, countS):
                while l < len(s) and l <= r and self.matchCount(countT, countS):
                    if len(res) == 0:
                        res = s[l: r + 1]
                    elif len(res) > len(s[l: r + 1]):
                        res = s[l: r + 1]
                    # print(f"countT : {countT}")
                    # print(f"countS: {countS}")
                    # print(f"res: {res}")
                    countS[s[l]] = countS.get(s[l], 0) - 1
                    if countS[s[l]] == 0:
                        del countS[s[l]]
                    l += 1
            print(l, r)
            r += 1

        return res



