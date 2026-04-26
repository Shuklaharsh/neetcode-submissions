class Solution:
    def bS(self, nums, target):
        
        l = 0
        r = len(nums) - 1
        while(l <= r):
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return True
        
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for nums in matrix:
            if self.bS(nums, target):
                return True
        
        return False