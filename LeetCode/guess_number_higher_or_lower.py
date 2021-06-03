
def guess(guessed_n:int) -> int:
    picked_num = 1
    if picked_num < guessed_n:
        return -1
    if picked_num > guessed_n:
        return 1
    return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        validate_guess = guess(n)
        if validate_guess == 0:
            return n
        return self.guess_from_list(1,n)

    def guess_from_list(self, first_num: int, last_num: int) -> int:
        middle_index = int((last_num - first_num)/2)
        middle_num = first_num + middle_index
        validate_guess = guess(middle_num)
        if validate_guess == 0:
            return middle_num
        elif validate_guess == -1:
            return self.guess_from_list(first_num=first_num, last_num=middle_num-1)
        return self.guess_from_list(first_num=middle_num+1, last_num=last_num)


a = Solution()
print(a.guessNumber(2))

2126753390
1702766719