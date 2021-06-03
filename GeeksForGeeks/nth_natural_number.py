class Solution:
    def findNth(self,N):
        final_number = ""
        while N:
            last_digit = N % 9
            final_number = str(last_digit) + final_number
            N = N // 9
        return final_number

a = Solution()
print(a.findNth(10))
