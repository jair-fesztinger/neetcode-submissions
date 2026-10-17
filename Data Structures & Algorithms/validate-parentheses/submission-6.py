class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        dict1 = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []

        for i in s:

            if i not in dict1:
                stack.append(i)
            elif not stack or stack[-1] != dict1[i]:
                return False
            else:
                stack.pop()
        return not stack
        

