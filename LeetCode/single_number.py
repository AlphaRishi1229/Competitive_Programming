from collections import Counter
import heapq

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        return heapq.nsmallest(1, count.keys(), key=count.get)