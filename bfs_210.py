from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pres = [set() for _ in range(numCourses)]
        posts = [set() for _ in range(numCourses)]
        for post, pre in prerequisites:
            posts[pre].add(post)
            pres[post].add(pre)
        queue = deque([i for i in range(numCourses) if not pres[i]])
        res = []
        while queue:
            i = queue.popleft()
            res.append(i)
            for j in posts[i]:
                pres[j].remove(i)
                if not pres[j]:
                    queue.append(j)
        return res if len(res) == numCourses else []