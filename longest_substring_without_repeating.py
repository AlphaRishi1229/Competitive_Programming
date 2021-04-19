class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        result = 0
        leftptr = 0
        for rightptr in range(len(s)):
            while s[rightptr] in charSet:
                charSet.remove(s[leftptr])
                leftptr += 1
            charSet.add(s[rightptr])
            result = max(result, rightptr - leftptr + 1)
        return result

soln = Solution()
print(soln.lengthOfLongestSubstring("abcabcbb"))