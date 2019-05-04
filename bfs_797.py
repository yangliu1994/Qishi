from collections import deque
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        lines = [{} for _ in range(n)]
        for start, end, dist in flights:
            lines[start][end] = dist
        queue = deque([(src, -1, 0)])
        res = float('inf')
        while queue:
            node, steps, cum = queue.popleft()
            if node == dst and cum < res:
                res = cum
                continue
            if cum >= res or steps == K:
                continue
            for nxt in lines[node]:
                queue.append((nxt, steps + 1, cum + lines[node][nxt]))
        return -1 if res == float('inf') else res

