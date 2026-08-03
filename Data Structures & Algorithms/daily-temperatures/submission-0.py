class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)
        res = [0] * N
        stack = []

        for i in range (N):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                popped = stack.pop()
                res[popped] = i - popped
            stack.append(i)

        return res

        