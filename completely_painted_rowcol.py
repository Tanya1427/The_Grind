"""
Understand.
mat[r][c] and arr[i] are unique.
m, n max is 10**5, m*n max is 10**5
 -> O(m*n) would work
 complete paint mean either m/n in a row/col are painted

Match.
Matrix. Hash Map. Counting.

Plan.
Brute force.
save all indices (r, c) in array len m*n + 1
painted = mat*0
for i, val in enumerate arr:
    r, c = indices[val]
    check up left down right in sucession if it's painted
        if not painted:
            break
    else:
        return i
PlanB
after 10 mins nap...
save indices like in brute force.
have a kind of multi-counter... initialize all to 0
when r, c is painted, increase r and c by 1
use an array or two, index r as 0 and c as 1
if increase reaches m|n return i (switch row/column count)

indices = [0] * (1 + mn)
loop through arr and save.
fill_count: [[0] * m, [0] * n]
for r, c in matrices:
    fill[0][r] += 1 # Same for [1],
    if == m/n return i

Implement.
"""
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n, mn = len(mat), len(mat[0]), len(arr)
        index = [0] * (1 + mn)
        paint_count = [[0] * m, [0] * n]
        # Make index
        for r in range(m):
            for c in range(n):
                index[mat[r][c]] = (r, c)

        for i, cell in enumerate(arr):
            r, c = index[cell]
            for first, second, end in ((0, r, n), (1, c, m)):
                paint_count[first][second] += 1
                if paint_count[first][second] == end:
                    return i

        return mn - 1  # Just in (impossible) case

"""
Review.
Failed testcase (forgot row/column comples)
[1,4,5,2,6,3]
[[x,3,5],
 [x,2,6]]

[0, (1, 0), (1, 1), (0, 1), (0, 0), (0, 2), (1, 2)]
[[1, 1], [2, 0, 0]]

Evaluate.
Space: O(mn). O(mn) for index, O(m + n) for paint_count
Time: O(mn). O(mn) for building. O(mn) (roughly) for finding i
"""