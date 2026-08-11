class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        map = {}
        for num in nums:
            if num not in map:
                map[num] = 1
            else:
                map[num] += 1
    
        desc = (sorted(map.items(), key=lambda item: item[1],
                reverse=True))

        res = []
        for i in range(k):
            res.append(desc[i][0])    
        return res
            