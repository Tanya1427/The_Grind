"""
Understand.
No need to check land. O(m**2 * n**2) would work as m, n | max is 10

Match.
BFS.

Plan.
loop through all rows cols with r, c.
Traverse to find fish sum if grid[r][c]
set max.
Each cell should be visited once.

Implement.
"""

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        rows, cols = range(len(grid)), range(len(grid[0]))
        queue = deque()
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))  # As per description.
        visited = [[False] * len(grid[0]) for _ in rows]
        max_fish = 0
        for r in rows:
            for c in cols:
                fish = grid[r][c]
                if not fish or visited[r][c]: continue
                queue.append((r, c))
                visited[r][c] = True
                while queue:
                    ri, ci = queue.popleft()
                    for dr, dc in dirs:
                        rx, cx = ri + dr, ci + dc
                        if not (rx in rows and cx in cols) or\
                         (not grid[rx][cx]) or visited[rx][cx]: continue
                        fish += grid[rx][cx]
                        visited[rx][cx] = True
                        queue.append((rx, cx))
                max_fish = max(max_fish, fish)

        return max_fish

"""
Reviewed.

Evaluate.
Space: O(m*n). Visited makes sure no multiple visits
Time: O(m*n). Visited makes sure no multiple visits
"""