class Solution:
    def MissingNumber(self,array,n):
        total_sum = (n * (n + 1))/2
        array_sum = sum(array)
        return int(total_sum - array_sum)


a = Solution()
print(a.MissingNumber([2], 2))
