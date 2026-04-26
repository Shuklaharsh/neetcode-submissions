class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Everything is sorted 1 2 3 4 5

        # We end up on lower mid 5 6 1 2 3 depending on target choose left or right
        # mid < left and mid < right
            # if target > mid and target < right:
                # choose right side
            # else
                # choose left side
        
        # We end up on higher mid 4 5 6 7 1 2
        # mid > left and mid > right
            # if target < mid and target < left:
                # choose right side
            # else 
                # choose left side
        # 4,5,6,7,0,1,2
        # 0,1,2,3,4,5,6
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif nums[mid] <= nums[right]:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target < nums[mid] and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return -1