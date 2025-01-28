# Modifying 2658. Find and replace area -> area  # HAHA!
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = range(len(grid)), range(len(grid[0]))
        queue = deque()
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))  # As per description.
        visited = [[0] * len(grid[0]) for _ in rows]
        max_area = 0
        for r in rows:
            for c in cols:
                area = grid[r][c]
                if not area or visited[r][c]: continue
                queue.append((r, c))
                visited[r][c] = 1
                while queue:
                    ri, ci = queue.popleft()
                    for dr, dc in dirs:
                        rx, cx = ri + dr, ci + dc
                        if not (rx in rows and cx in cols) or\
                         (not grid[rx][cx]) or visited[rx][cx]: continue
                        area += grid[rx][cx]
                        visited[rx][cx] = True
                        queue.append((rx, cx))
                max_area = max(max_area, area)

        return max_area
