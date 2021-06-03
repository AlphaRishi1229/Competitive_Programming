from typing import List


class Solution:
    def subarraySum(self, n: List[int], k: int) -> int:
        count = 0
        cumulative_sum = 0
        sum_map = {
            0: 1
        }
        for i in n:
            cumulative_sum += i
            if cumulative_sum - k in sum_map:
                count += sum_map[cumulative_sum - k]
            if cumulative_sum in sum_map:
                sum_map[cumulative_sum] += 1
            else:
                sum_map[cumulative_sum] = 1
            print(sum_map)
        return count


a = Solution()
print(a.subarraySum([1,2,3], 3))