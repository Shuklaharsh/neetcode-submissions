class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        n = len(nums) - 1 #3
        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1] 
            right[n - i] = right[n - i + 1] * nums[n - i + 1]

        res = []
        for i in range(len(nums)):
            res.append(left[i] * right[i])

        return res