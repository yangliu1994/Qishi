class Solution:
    def findOrder(self, numCourses, prerequisites):
        gh = [0 for i in range(numCourses)]
        ghin = [[] for i in range(numCourses)]
        res = []
        for (i, j) in prerequisites:
            gh[i] += 1
            ghin[j].append(i)
        self.bfs(gh, ghin, res)
        return res if len(res) == numCourses else []


    def bfs(self, gh, ghin, res):
        q = []
        for i, pre in enumerate(gh):
            if pre == 0:
                res.append(i)
                q.append(i)
        while q:
            t = q.pop(0)
            for j in ghin[t]:
                if gh[j] != 0:
                    gh[j] -= 1
                    if gh[i] == 0:
                        res.append(i)
                        q.append(i)
