from collections import deque
import string
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque()
        seen_words = set()
        set_of_words = set(wordList)

        if endWord not in set_of_words:
            return 0

        queue.append(beginWord)
        seen_words.add(beginWord)

        steps_taken = 0
        while len(queue) > 0:
            for _ in range(len(queue)):
                popped_element = queue.popleft()

                if popped_element == endWord:
                    return steps_taken + 1

                for i in range(len(popped_element)):
                    for char in string.ascii_lowercase[:26]:
                        new_word = popped_element[:i] + char + popped_element[i+1:]
                        if new_word not in seen_words and new_word in set_of_words:
                            queue.append(new_word)
                            seen_words.add(new_word)

            steps_taken += 1
        return 0


a = Solution()
print(a.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))