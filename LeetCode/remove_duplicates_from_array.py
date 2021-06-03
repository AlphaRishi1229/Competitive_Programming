class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        ptr1element = nums[0]
        ptr1pos = length = 0
        for i in range(1,len(nums)):
            if nums[i] != ptr1element:
                nums[ptr1pos+1] = nums[i]
                ptr1element = nums[ptr1pos+1]
                ptr1pos += 1
                length += 1
        return length+1