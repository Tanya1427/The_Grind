"""
994. Rotting Oranges

UMPIRE
0 == Empty (touch not)
1: Fresh == not yet visited
2: rotten - visited

MATCH
Matrix, BFS

PLAN:
Get all rottens (r, c)
count until queue is empty

IMPLEMENT:
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = -1
        m, n = len(grid), len(grid[0])
        dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))

        rotten = deque()
        fresh = set()

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    rotten.append((r, c))
                elif grid[r][c] == 1:
                    fresh.add((r, c))

        # Base case if there's no rotten
            # then no time elasps if no fresh
        # if not rotten and not fresh:
        if not (rotten or fresh):
            return 0

        while rotten:
            N = len(rotten)
            for _ in range(N):
                rot_r, rot_c = rotten.popleft()
                for dr, dc in dirs:
                    r, c = rot_r+dr, rot_c+dc
                    if r in range(m) and c in range(n) and grid[r][c] == 1:
                        grid[r][c] = 2
                        rotten.append((r, c))
                        fresh.remove((r, c))
            minutes += 1

        return -1 if fresh else minutes

"""
REVIEWed

EVALUATE:
Space: rotten, fresh --> O(n) (Worst case they won't even be cleared)
Time: O(m*n)

To remove fresh set, in the first for loop, check all around every 
fresh to see if it can be infected. If one can't be, return -1
HOLD ON!!! Can I REALLY know FOR SURE that I can just check once?
I think I'll leave the code like this.
"""
