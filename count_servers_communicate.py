"""
Understand.
line by line.
m, n max is 250 O(m**2 * n**2) will not work.

Match.
Matrix. Counting.

Plan.
First plan was wrong - my bad. Didn't understand the question.
count how many in every row and every column.
e.g. count = [[[0, 1, 2, 3]], [[0, 1, 2, 3]]]  # [*map(sum, row)]
count[0][r] is count of servers in row r
count[1][c] is count of servers in col c

next, loop throug all cells.
    if count of cell's row OR cell's column is more than 1:
        add to communicate

Implement
"""
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n, = len(grid), len(grid[0])
        count = [[0] * m, [0] * n]
        for r in range(m):
            for c in range(n):
                count[0][r] += grid[r][c]
                count[1][c] += grid[r][c]
        return sum(grid[r][c] and (count[0][r] > 1 or count[1][c] > 1) for r in range(m) for c in range(n))

"""
Review.
[[1,1,0,0],
 [0,0,1,0],
 [0,0,1,0],
 [0,0,0,1]]

Evaluate:
Space: O(m+n) for counter
Time: O(m*n)
"""