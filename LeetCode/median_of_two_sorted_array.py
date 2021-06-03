from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newList = sorted(nums1+nums2)
        if len(newList) % 2 == 0:
            median = (newList[int(len(newList)/2)-1] + newList[int(len(newList)/2)])/2
        else:
            median = newList[int(len(newList)/2)]
        return float(median)

soln = Solution()
print(soln.findMedianSortedArrays([1,3],[2]))