import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = right
        while(left <= right):
            mid = int((left + right) / 2)
            total_hours_taken = 0
            for num in piles:
                total_hours_taken += math.ceil(num/mid)
            
            if total_hours_taken > h:
                left = mid + 1
            elif total_hours_taken <= h:
                right = mid - 1
                ans = min(ans, mid)
        
        return ans