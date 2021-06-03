from typing import List

from collections import defaultdict

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        result = [0] * len(T)
        temp_stack = []
        for i in range(len(T)-1, -1, -1):
            while temp_stack and T[i] >= T[temp_stack[-1]]:
                temp_stack.pop()
            if temp_stack:
                result[i] = temp_stack[-1] - i
            temp_stack.append(i)

        return result



a = Solution()
print(a.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))