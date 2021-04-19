from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {i:nums[i] for i in range(len(nums))}
        result = []
        for i in range(len(nums)):
            nums_map.pop(i)
            value = target - nums[i]
            if value in list(nums_map.values()):
                key = list(nums_map.keys())[list(nums_map.values()).index(value)]
                result.append(i)
                result.append(key)
                return result


soln = Solution()
print(soln.twoSum([3,3],6))