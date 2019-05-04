from collections import deque
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        n = len(beginWord)
        if endWord not in wordList:
            return []
        dic = {}
        for i in range(n):
            dic[beginWord[:i] + '_' + beginWord[i + 1:]] = [beginWord]
        for word in wordList:
            for i in range(n):
                key = word[:i] + '_' + word[i + 1:]
                if key in dic:
                    dic[key].append(word)
                else:
                    dic[key] = [word]
        dist = {word: float('inf') for word in wordList}
        res = []
        queue = deque([[beginWord]])
        length = float('inf')
        while queue:
            temp = queue.popleft()
            if len(temp) > length:
                return res
            current = temp[-1]
            if current == endWord:
                res.append(temp)
                length = len(temp)
                continue
            if len(temp) == length:
                continue
            for i in range(n):
                for nxt in dic[current[:i] + '_' + current[i + 1:]]:
                    if nxt not in temp and len(temp) < dist[nxt]:
                        queue.append(temp + [nxt])
                        dist[nxt] = len(temp) + 1
        return res

