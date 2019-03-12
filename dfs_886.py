
class Solution:
    def possibleBipartition(self, N, dislikes):
        bag = [[] for i in range(N+1)]
        visited = [-1 for i in range(N+1)]
        count = 0
        for dislike in dislikes:
            bag[dislike[0]].append(dislike[1])
            bag[dislike[1]].append(dislike[0])
        for i in range(1, N+1):
            if not visited[i] and len(bag[i]):
                if not self.visit(0, i, bag, visited):
                    return False
        return True

    def visit(self, curLevel, i, bag, visited):
        if visited[i] >= 0:
            return (curLevel - visited[i]) % 2 == 0
        visited[i] = curLevel
        for j in bag[i]:
            if not self.visit(curLevel+1, j, bag, visited):
                return False
        return True

sol = Solution()

N = 4
dislikes = [[1,2],[1,3],[2,4]]

print(sol.possibleBipartition(N, dislikes))

N = 3
dislikes = [[1, 2], [1, 3], [2, 3]]

print(sol.possibleBipartition(N, dislikes))
