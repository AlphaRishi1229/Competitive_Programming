class Solution:
    def isHappy(self, n: int) -> bool:
        final_number = n
        squares = []
        while final_number != 1:
            final_number = self.getSquare(final_number)
            if final_number in squares:
                break
            else:
                squares.append(final_number)
        if final_number == 1:
            return True
        else:
            return False

    def getSquare(self, number: int) -> int:
        current_num = number
        square = 0
        while current_num != 0:
            remainder = current_num % 10
            left_number = current_num - remainder
            square += remainder * remainder
            current_num = left_number // 10
        return square

soln = Solution()
print(soln.isHappy(2))