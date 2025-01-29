"""
Understand.
1*k or k*1 - no need for b/dfs...

Match.
Matrix.

Plan.
set a total and count
count = 0
doubled = 0
traverse first row by row, and column by column.
when going through column, if beneath/above is a X, don't count.
if the count is 1, count as duplicate (doubled+=1) since it will be counted in the other traversal.

For the columns, check when you are at '.'
Do a check around to see if there is a column which is a ship

return total - doubled


Implement.
"""
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        rows, cols = range(m), range(n)
        total, doubled = 0, 0
        for r in rows:
            count = 0
            for c in cols:
                if board[r][c] == 'X':
                    count += 1
                    if (r < m - 1 and board[r + 1][c] == 'X') or\
                           (r > 0 and board[r - 1][c] == 'X'):
                        count = 0
                if board[r][c] == '.' or c == n - 1:
                    total += bool(count)
                    doubled += count == 1
                    count = 0

                if board[r][c] == '.' or r == m - 1:
                    rx = r - 1
                    if board[r][c] == 'X': rx = r                    
                    elif (r > 0 and board[r - 1][c] == '.' or r == 0): continue
                    total += not ((c < n - 1 and board[rx][c + 1] == 'X') or\
                                      (c > 0 and board[rx][c - 1] == 'X'))

        return total - doubled

"""
Review.
Was a lot of edge cases.

Evaluate
Space: O(1)
Time: O(m*n)
"""