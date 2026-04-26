class Solution:
    def trap(self, height: List[int]) -> int:
        
        
        # 0,2,0,3,1,0,1,3,2,1
        # 0,2,2,2,3,3,3,3,3,3
        # 3,3,3,3,3,3,3,3,1,0 


        # 4,2,0,3,2,5
        # 0,4,4,4,4,5
        # 5,5,5,5,5,0

        # 0,2,4,

        n = len(height)

        left_max = [0] * n
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(height[i], left_max[i - 1])

        print(left_max)

        right_max = [0] * n
        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1])

        print(right_max)
        ans = 0
        for i in range(1, n - 1):
            ans += max(0, (min(left_max[i], right_max[i]) - height[i]))

        return ans