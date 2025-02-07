"""
Understand.
Be careful not to rush understanding.

Match.
Hash Maps

Plan.
Keep hashmap of balls and colors.
balls will save the color of a specific ball.
colors will count how many of each colors have been encountered
defaultdict will be appropriate for colors.

set result to array of zeroes of len(queries)
iterate through enumeration, i=index, (x, y) in queries.
if x is not in balls yet,
 set balls[x] to y
 increment the number of colors, y
 increment, not set, because the color might already be present.
if it is in balls.
get it's current color (that's about to be replaced).
Decrease colors[current-x-color] by 1
if it's count reduces to 0, remove it from colors.
now set the new color of ball x, balls[x] = y
increment y.
Using a defaultdict for colors will ensure that if current-x-color == y:
    it will effectively be incremented (or set to 1 if it was deleted)
set results[i] to the length of colors.
Notice incrementing y twice? Do it once.
Notice setting balls[x] to y twice also? Do it once.

Implement.
"""
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls = {}
        colors = defaultdict(int)
        result = [0] * len(queries)
        for i, (x, y) in enumerate(queries):
            if x in balls:
                x_y = balls[x]
                colors[x_y] -= 1
                if not colors[x_y]: del colors[x_y]
            balls[x] = y
            colors[y] += 1
            result[i] = len(colors)
        return result

"""
Review.
Verified to increment colors not reset if new ball not in balls.
Noticed that operations in if and else where same.
Removed if x not in balls

Evaluate:
n = len(queries)
Space: O(n)
Time: O(n)
"""
