from typing import List

class SolutionOLD:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num_dict = {i:nums.count(i) for i in nums}
        soln_set = []
        ptr = 0
        seen = set()
        while ptr < len(nums)-1:
            if nums[ptr] not in seen:
                seen.add(nums[ptr])
                temp_dict = num_dict.copy()
                temp_dict[nums[ptr]] -= 1
                next_seen = set()
                i = ptr+1
                while i < len(nums)-1:
                    if nums[i] not in next_seen:
                        next_seen.add(nums[i])
                        temp_dict[nums[i]] -= 1
                        two_sum = nums[ptr] + nums[i]
                        req_val = 0 - two_sum
                        if temp_dict.get(req_val,0) >= 1:
                            triplet = sorted([nums[ptr], nums[i], req_val])
                            if triplet not in soln_set:
                                soln_set.append(triplet)
                    i += 1
            ptr += 1
        return soln_set


class Solutions:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        gotfirstpos = False
        first_pos = 0
        num_dict = {}
        for i in nums:
            if i > 0 and not gotfirstpos:
                gotfirstpos = True
                first_pos = i
            num_dict[i] = nums.count((i))
        soln_set = []
        three_sum = 0
        ptr = 0
        seen = set()
        zeroth_pos = nums.index(first_pos) if gotfirstpos else len(nums)-1
        while ptr < zeroth_pos:
            if nums[ptr] not in seen:
                seen.add(nums[ptr])
                temp_dict = num_dict.copy()
                temp_dict[nums[ptr]] -= 1
                i = ptr+1
                two_sum = three_sum - nums[ptr]
                next_seen = set()
                while i < len(nums)-1:
                    if nums[i] not in next_seen:
                        next_seen.add(nums[i])
                        temp_dict[nums[i]] -= 1
                        temp_sum = nums[ptr] + nums[i]
                        req_val = 0 - temp_sum
                        if temp_dict.get(req_val,0) >= 1:
                            triplet = sorted([nums[ptr], nums[i], req_val])
                            if triplet not in soln_set:
                                soln_set.append(triplet)
                    i += 1
            ptr += 1
        return len(nums)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()
        three_sum = 0
        for i, val1 in enumerate(nums):
            if val1 in seen:
                continue
            seen.add(val1)
            two_sum = three_sum - val1
            val2_set = set()
            for val3 in nums[i+1:]:
                    val2 = two_sum - val3
                    if val2 in val2_set:
                        res.append(sorted((val1, val2, val3)))
                    val2_set.add(val3)
        return res
#[-4, -3, -2, -1, -1, 0, 0, 1, 2, 3, 4]
soln = Solution()

print(soln.threeSum(sorted([-4, -3, -2, -1, -1, 0, 0, 1, 2, 3, 4])))

# -4+1 = -3
# 0-(-3) = 3