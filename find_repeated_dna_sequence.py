from collections import defaultdict
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        else:
            seen = defaultdict(int)
            for index in range(10, len(s)+1):
                sub_str = s[index-10:index]
                seen[sub_str] += 1
            seen_multiple_times = lambda key: seen[key] > 1

        return list(filter(seen_multiple_times, seen.keys()))


a = Solution()
print(a.findRepeatedDnaSequences("AAAAAAAAAAAAA"))