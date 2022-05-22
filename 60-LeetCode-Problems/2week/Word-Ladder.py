from collections import deque
from typing import Deque, List, Set


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordSet: Set[str] = set(wordList)
        temp: Deque = deque()
        temp.append((beginWord, 1))
        s = set()
        s.add(beginWord)

        while temp:
            now, cnt = temp.popleft()

            if now == endWord:
                return cnt

            for c1 in range(len(now)):
                for c2 in range(97, 123):
                    temp_word = now[:c1] + chr(c2) + now[c1 + 1:]
                    if temp_word in wordSet and temp_word not in s:
                        s.add(temp_word)
                        temp.append((temp_word, cnt + 1))
        return 0
