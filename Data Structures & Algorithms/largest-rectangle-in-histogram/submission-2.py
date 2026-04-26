class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # pairs (start_index, height)
        ans = 0
        n = len(heights)

        for i, h in enumerate(heights):
            start = i
            # pop taller bars, update answer and earliest start
            while stack and stack[-1][1] > h:
                idx0, h0 = stack.pop()
                ans = max(ans, h0 * (i - idx0))
                start = idx0  # new bar can extend to idx0
            # push the current bar with its correct leftmost start
            stack.append((start, h))

        # remaining bars extend to the end (width = n - start)
        while stack:
            idx0, h0 = stack.pop()
            ans = max(ans, h0 * (n - idx0))

        return ans
