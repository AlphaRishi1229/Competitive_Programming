class SolutionRecursion:
    def trailingZeroes(self, N):
        zeros = 0
        fact = self.calculate_fact(N)
        while fact % 10 == 0:
            zeros += 1
            fact = fact // 10
        return zeros

    def calculate_fact(self, N):
        if N == 0:
            return 1
        return N * self.calculate_fact(N-1)


class Solution:
    def trailingZeroes(self, N):
        zeros = 0
        while N > 0:
            N = N // 5
            zeros += N
        return zeros


a = Solution()
print(a.trailingZeroes(1000))