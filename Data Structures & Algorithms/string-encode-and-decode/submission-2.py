class Solution:

    def encode(self, strs: List[str]) -> str:
        # encoding is to identify the separation
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + '#' + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        
        while i < len(s):
            len_s = ''
            j = i
            while s[j] != '#':
                len_s += s[j]
                j += 1
            res.append(s[j + 1 : j + 1 + int(len_s)])
            i = j + 1 + int(len_s)
        
        return res
            
            