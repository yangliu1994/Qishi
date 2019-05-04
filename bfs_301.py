from collections import deque
from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = []
        queue = deque([s])
        length = 0

        def isValid(string):
            count1 = 0
            count2 = 0
            for l in string:
                if l == '(':
                    count1 += 1
                elif l == ')':
                    count2 += 1
                    if count2 > count1:
                        return 1
            if count1 == count2:
                return 0
            if count1 > count2:
                return 2
            if count1 < count2:
                return 1

        while queue:
            string = queue.popleft()
            if len(string) < length:
                break
            check = isValid(string)
            if check == 0:
                res.append(string)
                length = len(string)
            if len(string) == length:
                continue
            for i in range(len(string)):
                if check == 1 and string[i] == ')' and string[:i] + string[i + 1:] not in queue:
                    queue.append(string[:i] + string[i + 1:])
                elif check == 2 and string[i] == '(' and string[:i] + string[i + 1:] not in queue:
                    queue.append(string[:i] + string[i + 1:])
        return res
