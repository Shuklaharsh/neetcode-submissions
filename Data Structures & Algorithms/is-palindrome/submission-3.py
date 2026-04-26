class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        i = 0
        j = len(s) - 1
        s = s.lower()
        while i < j:
            if (ord('a') <= ord(s[i]) <= ord('z')) or (ord('0') <= ord(s[i]) <= ord('9')):
                if (ord('a') <= ord(s[j]) <= ord('z')) or (ord('0') <= ord(s[j]) <= ord('9')):
                    if s[i] != s[j]:
                        return False
                    else:
                        i += 1
                        j -= 1
                else:
                    j -= 1
            else:
                i += 1

        return True