class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0

        l, r = 0, len(heights) - 1

        while l < r:
            if heights[l] < heights[r]:
                ans = max(ans, (r - l) * heights[l])
                l += 1
            else:
                ans = max(ans, (r - l) * heights[r])
                r -= 1
        
        return ans