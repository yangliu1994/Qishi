
class Solution:
    def numIslands(self, graph):
        count = 0
        for i in range(len(graph)):
            for j in range(len(graph[0])):
                if graph[i][j] == 1:
                    self.dfs(graph, i, j)
                    count += 1
        return count

    def dfs(self, graph, i, j):
        if i < 0 or i >= len(graph) or j < 0 or j >= len(graph[0]) or graph[i][j] != 1:
            return
        graph[i][j] = -1
        self.dfs(graph, i-1, j)
        self.dfs(graph, i+1, j)
        self.dfs(graph, i, j-1)
        self.dfs(graph, i, j+1)

sol = Solution()

mat = [[1, 1, 0, 0, 0],
       [0, 1, 0, 0, 1],
       [1, 0, 0, 1, 1],
       [0, 0, 0, 0, 0],
       [1, 0, 1, 0, 1]]
print(sol.numIslands(mat))


