class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        l = 0
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - 97] += 1
            s2Count[ord(s2[i]) - 97] += 1
        
        for r in range(len(s1), len(s2)):
            if s1Count == s2Count:
                return True
            s2Count[ord(s2[l]) - 97] -= 1
            l += 1
            s2Count[ord(s2[r]) - 97] += 1
            
        return s1Count == s2Count