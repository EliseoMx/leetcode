class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checks = {}
        for i, num in enumerate(nums):
            validate = target - num
            if validate in checks:
                return[checks[validate],i]
            checks[num] = i
