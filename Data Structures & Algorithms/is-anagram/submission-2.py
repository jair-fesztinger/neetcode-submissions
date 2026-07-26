from collections import Counter 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_d = Counter(s)
        t_d = Counter(t)

        if s_d == t_d:
            return True
        else:
            return False