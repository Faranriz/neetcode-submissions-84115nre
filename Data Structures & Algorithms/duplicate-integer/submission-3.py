class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        count = defaultdict(int)

        for i in range(len(nums)):
            if nums[i] in count:
                return True
            count[nums[i]] = 1
        return False


            