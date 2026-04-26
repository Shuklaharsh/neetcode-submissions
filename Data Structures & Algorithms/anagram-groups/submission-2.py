class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        ans = []
        for s in strs:
            freq_count = [0] * 26
            for i in s:
                freq_count[ord(i) - ord('a')] += 1
            res[tuple(freq_count)].append(s)
        for i in res: 
            ans.append(res[i])
        return ans
        
               