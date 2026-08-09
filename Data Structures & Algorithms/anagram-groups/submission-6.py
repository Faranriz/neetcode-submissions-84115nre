class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for word in strs:
            count = [0] * 26
            for char in word:
                pos = ord(char) - 97
                count[pos] += 1

            if tuple(count) not in res:
                res[tuple(count)] = []
            res[tuple(count)].append(word)
        return list(res.values())