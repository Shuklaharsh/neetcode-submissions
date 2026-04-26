class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in ans:
                return [ans.get(diff), i]
            ans[nums[i]] = i