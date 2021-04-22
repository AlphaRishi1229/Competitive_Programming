from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        string_dict = Counter(s)
        list_in_desc = sorted(string_dict, key=string_dict.get, reverse=True)
        final_string = ""
        for string in list_in_desc:
            final_string += string * int(string_dict[string])
        return final_string


a = Solution()
print(a.frequencySort("Aabb"))