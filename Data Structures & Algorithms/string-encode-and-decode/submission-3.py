class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + "#" + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while(i < len(s)):
            l = ''
            while(s[i] != '#'):
                l += s[i]
                i += 1
            print(l)
            l = int(l)
            res.append(s[i + 1 : i + 1 + l])
            i = i + l + 1
        return res