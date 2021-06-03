from typing import List


class Solution:
    def smallestpositive(self, array: List, n):
        array.sort()
        smallest_integer = 1
        for number in array:
            if number <= smallest_integer:
                smallest_integer += number
            else:
                break
        return smallest_integer

a = Solution()
print(a.smallestpositive([1, 10, 3, 11, 6, 15],6))
