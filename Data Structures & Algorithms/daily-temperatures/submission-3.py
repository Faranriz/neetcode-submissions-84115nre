class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)
        stack = [] # adding pair values of [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                T, I = stack.pop()
                res[I] = i - I
            stack.append([t, i])
        
        return res