import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        k = re.sub(r"[^a-z0-9]", "", s.lower())
        i, j = 0, len(k) - 1

        if len(k) == 0:
            return True

        while i < j:
            if k[i] != k[j]:
                return False
            i += 1
            j -= 1
        
        return True
            

       

