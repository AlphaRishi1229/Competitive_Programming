class Solution:
    def fractionToDecimal(self, numerator, denominator):
        if numerator % denominator != 0:
            final_result = ""
            final_result += str(numerator//denominator)
            final_result += "."
            remainder_map = {}
            remainder = numerator % denominator
            while remainder != 0 and remainder not in remainder_map:
                remainder_map[remainder] = len(final_result)
                remainder *= 10
                res = remainder // denominator
                final_result += str(res)
                remainder = remainder % denominator
            if remainder == 0:
                return final_result
            else:
                return (final_result[:remainder_map[remainder]] + "(" + final_result[remainder_map[remainder]:] + ")")
        else:
            return numerator // denominator

def recurring_decimal(numerator, denominator):
    final_result = ""
    remainder_map = {}
    remainder = numerator % denominator
    while remainder != 0 and remainder not in remainder_map:
        remainder_map[remainder] = len(final_result)
        remainder *= 10
        res = remainder // denominator
        final_result += str(res)
        remainder = remainder % denominator
    if remainder == 0:
        return "No recurring remainders"
    else:
        return final_result[remainder_map[remainder]:]


a = Solution()
print(a.fractionToDecimal(2,3))
#print(recurring_decimal(2, 3))