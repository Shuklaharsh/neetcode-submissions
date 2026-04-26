class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n

        1, 1, 2, 8
        for i in range(1, n):
            ans[i] = ans[i - 1] * nums[i - 1]
        
        suffix = 1
        for i in range(n - 1, -1, -1):
            ans[i] = suffix * ans[i]
            suffix = suffix * nums[i]

        return ans 


        