"""
Understand.
n max = 100, O(n*m) will work.

Match.
BFS.

Plan.
Follow hint.
Graph of (0, 0) to (m-1, n-1)
Adjancency list to represent right left down up,
 and 0/1 to represent weight
Use a 2(3)d array to make adjacency list
[(0, (0, 1)), ...]

Run Djikstra's on the graph and return graph[m - 1][n - 1]

Implement
"""
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}
        graph = [0] * m
        costs = [0] * m
        visited = [0] * m

        # Traverse round for all in matrix to build graph.
        # Also add the costs and visited defaults
        for r in range(m):
            costs[r] = [float("inf")] * n
            visited[r] = [0] * n
            graph[r] = [0] * n
            for c in range(n):
                dir_rc = dirs[grid[r][c]]
                graph[r][c] = []
                for dr, dc in dirs.values():
                    rx, rc = r + dr, c + dc
                    cost = 1 - ((dr, dc) == dir_rc)
                    if rx in range(m) and rc in range(n):
                        graph[r][c].append((cost, (rx, rc)))

        # Now run Djikstra's
        pq = [(0, (0, 0))]
        costs[0][0] = 0
        while pq:
            cost, (r, c) = heappop(pq)
            # Return early if reached end.
            if (r, c) == (m - 1, n - 1):
                return costs[r][c]
            visited[r][c] = 1
            for costx, (rx, cx) in graph[r][c]:
                if visited[rx][cx] or costx + cost >= costs[rx][cx]: continue
                costs[rx][cx] = costx + cost
                heappush(pq, (costs[rx][cx], (rx, cx)))

        # Just in case.
        return costs[m - 1][n - 1]

"""
Reviewed.

Evaluate:
Space: O(mn)  # For graph, costs, and visited
Time: O(mnlogmn), 4nm for building graph. mnlogmn =>for djs
(log mn > 4 as mn gets big.)
"""