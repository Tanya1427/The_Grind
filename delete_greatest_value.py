"""
Understand:
Remove largest number until empty.
Can input be empty - not entiriely.
largest is 1000

Match:
Sorting. Heaps.

Plan.
plan1:
sort each row.
get of each column. and add to score.

Plan2:
heapify each row.
Heappop max and update with largest
add largest to score
"""
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        score = 0
        for row in grid:
            row.sort()
        m = len(grid)
        n = len(row)

        for c in range(n):
            largest = float("-inf")
            for r in range(m):
                largest = max(largest, grid[r][c])
            score += largest
        
        return score

    def deleteGreatestValueHeap(self, grid: List[List[int]]) -> int:
        score = 0
        for row in grid:
            heapq._heapify_max(row)
        m = len(grid)
        n = len(row)

        for _ in range(n):
            largest = float("-inf")
            for row in grid:
                largest = max(largest, heapq._heappop_max(row))
            score += largest

        return score
"""
Reviewed

Evaluate:
sorting: m = rows, n = cols.
O(nmlogm) + O(mn) == O(mnlogm)
Heaping.
O(nm) + O(mnlogm) == O(mnlogm) => But m keeps reducing, though! logm, log(m-1), etc.
Might be better.
"""
