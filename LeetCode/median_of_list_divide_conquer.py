from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        sorted_list = self.sort_list(nums1)
        middle_index = int(len(sorted_list)/2)
        if len(sorted_list) % 2 == 0:
            median = (sorted_list[middle_index-1] + sorted_list[middle_index])/2
        else:
            median = sorted_list[middle_index]
        print(median)
        return median

    def sort_list(self, unsorted_list: List) -> List:
        if len(unsorted_list) < 2:
            return unsorted_list
        else:
            middle_index = int(len(unsorted_list)/2)
            pivot_element = unsorted_list[middle_index]
            less_than_pivot = [i for i in unsorted_list[:middle_index] + unsorted_list[middle_index+1:] if i <= pivot_element]
            greater_than_pivot = [i for i in unsorted_list[:middle_index] + unsorted_list[middle_index+1:] if i > pivot_element]
            return self.sort_list(less_than_pivot) + [pivot_element] + self.sort_list(greater_than_pivot)


# a = Solution()
# a.findMedianSortedArrays([1,3],[2])

import random

def quick_sort(array: List) -> List:
    array_length = len(array)
    if array_length < 2:
        return array
    else:
        pivot_index = random.choice([x for x in range(0, array_length)])
        less_than_pivot = [val for val in array[:pivot_index]+array[pivot_index+1:] if val <= array[pivot_index]]
        greater_than_pivot = [val for val in array[:pivot_index]+array[pivot_index+1:] if val > array[pivot_index]]
        return quick_sort(less_than_pivot) + [array[pivot_index]] + quick_sort(greater_than_pivot)

print(quick_sort([3,2,1,5,8,6,3,10]))
