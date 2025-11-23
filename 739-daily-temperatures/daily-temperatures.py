class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                prev = stack.pop()
                res[prev] = i - prev
            stack.append(i)

        return res


# Driver code (must be written AFTER class Solution)
param_1 = [73,74,75,71,69,72,76,73]
ret = Solution().dailyTemperatures(param_1)
print(ret)
