class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        LAND = '1'
        WATER = '0'
        deltas = ((-1, 0), (0, 1), (1, 0), (0, -1))
        m = len(grid)
        n = len(grid[0])
        count = 0
        def bfs(r, c):
            grid[r][c] = WATER
            queue = deque()
            queue.append((r, c))
            while queue:
                r, c = queue.popleft()
                for dr, dc in deltas:
                    nr, nc = r+dr, c+dc
                    if nr in range(m) and nc in range(n) and grid[nr][nc] == LAND:
                        grid[nr][nc] = WATER
                        queue.append((nr, nc))
            return 1
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == LAND:
                    count += bfs(r, c)

        return count
