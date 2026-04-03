class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # 2 pointers
        lp, rp = 0, len(s) - 1
        
        while lp < rp:
            if not s[lp].isalnum():
                lp += 1
                continue        # to skip to next iteration
            if not s[rp].isalnum():
                rp -= 1
                continue

            if not s[lp].lower() == s[rp].lower():
                return False

            lp += 1
            rp -= 1
            
        return True