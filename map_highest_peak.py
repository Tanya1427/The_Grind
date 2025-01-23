"""
Understand.
adjacent height diff == 1

Match.
BFS

Plan.
add all water cells to queue first.
do bfs starting with first water cell.
if neighbouring cell is out of bounds, water, or already has height set, leave it.
else add it to queue and make it's height 1 + its parent height.

Implement
"""
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))
        height = [[0] * n for _ in range(m)]
        queue = deque()
        for r in range(m):
            for c in range(n):
                if isWater[r][c]:
                    queue.append((r, c))
        while queue:
            r, c = queue.popleft()
            for dr, dc in dirs:
                rx, cx = r + dr, c + dc
                if not (rx in range(m) and cx in range(n))\
                    or isWater[rx][cx] or height[rx][cx]:   continue
                height[rx][cx] = 1 + height[r][c]
                queue.append((rx, cx))

        return height
                    
            
"""
Review.
queue = (2, 1)
isWater    height
[0, 0, 1]  [1, 1, 0]
[1, 0, 0]  [0, 1, 1]
[0, 0, 0]  [1, 2, 2]

Evaluate.
Space: O(m*n) for queue (not counting return value)
Time: O(m*n) => Not visiting already visited cells...
"""
