class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = [0] * 26
        l = 0
        res = 0

        for r, c in enumerate(s):
            count[ord(c) - 65] += 1
            highest_freq = max(count)
            while ((r - l + 1) - highest_freq) > k:
                count[ord(s[l]) - 65] -= 1
                l += 1
            res = max((r - l + 1), res)
        return res