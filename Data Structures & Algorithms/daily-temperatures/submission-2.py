class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)


        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                distance = abs(stack[-1][0] - i)
                result[stack[-1][0]] = distance
                stack.pop()
            
            stack.append((i,t))

        stack.append((0, temperatures[0]))

        return result