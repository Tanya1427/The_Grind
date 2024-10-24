"""
Understand
Get sum of region...
No input will be out of bounds. Range Sum Query - Immutable pro.

Match:
Prefix sum upon prefix sum :).

Plan:
(Which an interviewer told me :) )
Get sums from (0, 0) for all row/cols - and store
e.g
From
[3, 0, 1, 4]
[5, 6, 3, 2]
[1, 2, 0, 1]
[4, 1, 0, 1]

Get
[3,   3,   4,   8]
[8,  14,  18,  24]
[9,  17,  21,  28]
[13, 22,  26,  34]

How?
Do prefix sum of all rows and all columns?

For all rows.
[3,  3,  4,  8]
[5, 11, 14, 16]
[1,  3,  3,  4]
[4,  5,  5,  6]

Now do prefix sum column-wise
[3, 3, 4, 8]
[8, 14, 18, 24]
[9, 17, 21, 28]
[13, 22, 26, 34]

That worked.

Now, after that, how to get any row1, col1, row2, col2 
It's going to be hard now :)
[3,   3,   4,   8]
[8,  14,  18,  24]
[9,  17,  21,  28]
[13, 22,  26,  34]
get from (1, 1) => (2, 2)
You should be able to get any sum from sums from (0, 0)
Timestamp. Funnily: 12:46pm, did this same time for another question twelve hours ago.
(1, 1) => (2, 2)

((0, 0) => (2, 2)) - ((0, 0) => (0, 2))
 - ((0, 0) => (2, 0)) + ((0, 0)=>(0,0))

(0, 0) to (row2, col2)
-(0, 0) to (row1-1, col2)
-(0, 0) to (row2, col1-1)
+(0, 0) to (row1-1, col1-1)
to check >0, use the value 0==False
Implement
"""

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # Make prefix sum. Do not use additional space.
        m, n = len(matrix), len(matrix[0])
        # For the rows
        for row in matrix:
            for c in range(1, n):
                row[c] += row[c-1]
        # for the 'columns'
        for r in range(1, m):
            for c in range(n):
                matrix[r][c] += matrix[r-1][c]

        self.sums = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        full = self.sums[row2][col2]
        top = row1 and self.sums[row1-1][col2]
        right = col1 and self.sums[row2][col1-1]
        intersection = row1 and col1 and self.sums[row1-1][col1-1]
        return full-top-right+intersection

"""
Reviewed ish

Evaluate:
Space: O(1)
Time: O(mn) for initializing self.sums. O(1) for doing sumRegions

"""

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
