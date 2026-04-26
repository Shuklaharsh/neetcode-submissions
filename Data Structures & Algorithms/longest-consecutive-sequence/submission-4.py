class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0

        store = set(nums)

        ans = 1
        for num in nums:
            if (num - 1) in store:
                continue
            length = 1
            while (num + 1) in store:
                length += 1
                num += 1
                ans = max(length, ans)
        
        return ans