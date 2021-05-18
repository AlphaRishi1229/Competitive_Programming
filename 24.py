from typing import List

class Solution:
    def __init__(self):
        self.middle_index = 0
        self.current_index = 0

    def search(self, nums: List[int], target: int) -> int:
        middle_index = int(len(nums)/2)
        middle_value = nums[middle_index]
        if not self.middle_index:
            self.middle_index = middle_index

        if len(nums) == 1 and middle_value != target:
            return -1
        elif middle_value == target:
            final_idx = self.middle_index + self.current_index
            return final_idx
        elif target > nums[0] and target < middle_value:
            self.current_index -= int(len(nums[:middle_index])/2)
            return self.search(nums[:middle_index], target)
        else:
            self.current_index += int(len(nums[middle_index:])/2)
            return self.search(nums[middle_index:], target)


a = Solution()
print(a.search([4,5,6,7,0,1,2], 7))
