class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has_set_seen = set()

        for i in nums:
            if i in has_set_seen:
                return True
            has_set_seen.add(i)
        
        return False

         