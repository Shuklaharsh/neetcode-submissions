class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        res = 0
        while(l < r):
            curr_min_height = 1
            if heights[l] < heights[r]:
                curr_min_height = heights[l]
                l += 1
            else:
                curr_min_height = heights[r]
                r -= 1

            res = max(res, curr_min_height * (r - l + 1))

        return res
