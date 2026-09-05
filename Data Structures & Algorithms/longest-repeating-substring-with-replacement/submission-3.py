class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count = [0] * 26
        l = 0
        for r in range(len(s)):
            count[ord(s[r]) - 65] += 1
            highest_freq = max(count)
            while (r - l + 1) - highest_freq > k:
                count[ord(s[l]) - 65] -= 1
                l += 1
            res = max(res, r - l + 1) 
        return res