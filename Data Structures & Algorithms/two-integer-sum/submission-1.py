class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i, num in enumerate(nums):
            diff = target - num 
            if diff not in map:
                map[num] = i
            else:
                return [map[diff], i]
