class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l = 0
        r = len(numbers) - 1
    
        while True:
            if int(numbers[l]) + int(numbers[r]) > target:     
                r -= 1
            elif int(numbers[l]) + int(numbers[r]) < target:
                l += 1
            elif int(numbers[l]) + int(numbers[r]) == target:
                l, r = l + 1, r + 1
                break
        
        return [l, r]
