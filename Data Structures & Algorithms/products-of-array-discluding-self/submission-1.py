class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left_product = [0] * len(nums)
        left_product[0] = 1
        for i in range(1, len(nums)):
            left_product[i] = left_product[i-1] * nums[i - 1]
        
        
        right_product = [0] * len(nums)
        right_product[len(nums) - 1] = 1
        for i in range(len(nums) - 2, -1, -1):
            right_product[i] = right_product[i + 1] * nums[i + 1]

        # 1, 1, 2, 8
        # 48, 24, 6, 1

        ans = []
        for i in range(0, len(nums)):
            res = left_product[i] * right_product[i]
            ans.append(res)

        return ans
