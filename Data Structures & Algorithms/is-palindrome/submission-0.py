class Solution:
    def isPalindrome(self, s: str) -> bool:
        #remove non-alphanumeric and lowercase
        s = "".join(char.lower() for char in s if char.isalnum())
        # pointer that looks at string from RHS
        
        p = len(s) - 1
        for idx, letter in enumerate(s):
            if not letter == s[p - idx]:
                return False
        return True
    
       