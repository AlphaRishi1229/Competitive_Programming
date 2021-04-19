from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_collection = defaultdict(list)
        for str in strs:
            final_collection[tuple(sorted(str))].append(str)

        return final_collection.values()


a = Solution()
print(a.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))