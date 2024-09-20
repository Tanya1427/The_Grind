"""
944. Delete Columns to Make Sorted

You are given an array of n strings strs, all of the same length.

The strings can be arranged such that there is one on each line, making a grid.

For example, strs = ["abc", "bce", "cae"] can be arranged as follows:
                        a b c
                        b c e
                        c a e
You want to delete the columns that are not sorted lexicographically.
In the above example (0-indexed), columns 0 ('a', 'b', 'c')
 and 2 ('c', 'e', 'e') are sorted, while column 1 ('b', 'c', 'a') is not,
  so you would delete column 1.

Return the number of columns that you will delete.

  

Example 1:

Input: strs = ["cba","daf","ghi"]
Output: 1
Explanation: The grid looks as follows:
  cba
  daf
  ghi
Columns 0 and 2 are sorted, but column 1 is not, so you only need to delete 
1 column.
Example 2:

Input: strs = ["a","b"]
Output: 0
Explanation: The grid looks as follows:
  a
  b
Column 0 is the only column and is sorted, so you will not delete any columns.
Example 3:

Input: strs = ["zyx","wvu","tsr"]
Output: 3
Explanation: The grid looks as follows:
  zyx
  wvu
  tsr
All 3 columns are not sorted, so you will delete all 3.
 

Constraints:

n == strs.length
1 <= n <= 100
1 <= strs[i].length <= 1000
strs[i] consists of lowercase English letters.

    c b a
    d a f
    g h i


        a
        b
    imi
    tim
    mig
    jas

i, j
0, 0
0, 1
0, 2

1, 0
1, 1
1, 2

2, 0
2, 1
2, 2

3, 0
3, 1
3, 2

Match:
Matrix. String. Array. Binary search (matrix graph connection)

Plan:
- Get  the columns
- loop | comparing the ith of each as we go
- [compare]

1,2,4,5
[cba, daf, ghi, jqu]
        cba
        daf
        ghi
        jqu

ch = 'a'
b
a
c
n = len(strs) -> 4
m = len(strs[i]) -> 3
count = 0
prev = 'a'
for c in range(m):
    for r in range(n):
        next = strs[r][c]
        if prev > next:
            count += 1
            break
        else:
            prev = next

return count

[]
0, 0
1, 0
2, 0
3, 0

0, 1
1, 1
2, 1
3, 1

UMPIRME
IMPLEMENT:
"""
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        count = 0
        for c in range(m):
            prev = 'a'
            for r in range(n):
                next = strs[r][c]
                if prev > next:
                    count += 1
                    break
                else:
                    prev = next
        return count

"""
Review:
a b c
b y e
c z g 

strs[0][0] -> strs[3][0]
abc
byz
ceg
n = 4
m = 3

    count = 0
    prev = 'j'
    c = 1
        r = 0
        next = c

[1, 2, 3, 4, 5, 6, 7]
"""