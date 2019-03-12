
class Solution:
    def longestCable(self, graph, n):
        maxLen = -9999999999
        for i in range(1, n+1):
            visited = [False] * (n + 1)
            self.dfs(graph, i, 0, maxLen, visited)
        return maxLen

    def dfs(self, graph, i, curLevel, maxLen, visited):
        visited[i] = True
        adjacent = None
        for j in range(len(graph[i])):
            adjacent = graph[i][j]
            if not visited[i]:
                nextlevel = curLevel + adjacent[1]
                self.dfs(graph, adjacent[0], nextlevel, maxLen, visited)
            if maxLen < nextlevel:
                maxlen = nextlevel
        