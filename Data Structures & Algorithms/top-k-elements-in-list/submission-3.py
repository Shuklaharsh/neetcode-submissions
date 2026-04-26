class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            res[c].append(n)

        ans = []
        for i in range(len(res) - 1, 0 , -1):
            for num in res[i]:
                ans.append(num)
            if len(ans) == k:
                return ans

        return ans
       