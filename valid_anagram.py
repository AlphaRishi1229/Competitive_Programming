
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if list(sorted(t)) == list(sorted(s)):
            return True
        else:
            return False


a = Solution()
print(a.isAnagram("anagram","nagaram"))