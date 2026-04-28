"""
Understand.
 [[3, 4], [7, 81, [2, 5], [6, 7), [1, 4] => [1, 5], [6, 8]
Start can be 0. end is up to 10k
they are closed intervals.


Match: Intervals, sorting

Plan.
Sort.
 [[3, 4], [7, 8], [2, 5], [6, 7], [1, 4] => [1, 5], [6, 8]

[1, 4], [2, 5], [3, 4], [6, 7], [7, 8]

Overlaps:
end <= start

ans = [[1, 5], ]
merged = [6, 8]
move intrvl throgh intervals
    does merge  overlap with intrvl
    Yes: merge them
        merged = [smallest of the firsts, largest of the lasts]
    No: Add merged to answer, set merged as intrvl
        ans.push(merged)
        merged = intrvl
ans.push()
[2, 7]
[5, 15]
 |
 |
\ /
[2, 15]
[2, 7], [4, 6]

2, 7

Implement
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]
        for interval in intervals:
            if ans[-1][1] >= interval[0]:
                ans[-1][1] = max(ans[-1][1], interval[1])
            else:
                ans.append(interval)
        return ans

"""
Reviewed.

Evaluate.
Space: O(1) not counting output
Time => O(n log n)
"""
